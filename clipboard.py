import os
import shutil
import subprocess
import sys
import time
import unicodedata

import pyautogui


def detect_encoding(path):
    with open(path, "rb") as f:
        raw = f.read()
    try:
        import chardet

        result = chardet.detect(raw)
        return result.get("encoding") or "utf-8"
    except Exception:
        return "utf-8"


def paste_text(text):
    txt = unicodedata.normalize("NFC", str(text))

    def set_clipboard_with_fallback(s):
        try:
            import pyperclip

            pyperclip.copy(s)
            return True
        except Exception:
            pass

        enc = s.encode("utf-8")

        # platform-specific helpers
        if sys.platform.startswith("darwin"):
            # macOS: pbcopy
            if shutil.which("pbcopy"):
                try:
                    subprocess.run(["pbcopy"], input=enc, check=True)
                    return True
                except Exception:
                    pass
        elif sys.platform.startswith("win"):
            # Windows: clip.exe
            if shutil.which("clip"):
                try:
                    # clip reads from stdin
                    subprocess.run(["clip"], input=enc, check=True, shell=False)
                    return True
                except Exception:
                    pass
            # try PowerShell Set-Clipboard as fallback
            try:
                subprocess.run(
                    ["powershell", "-Command", "Set-Clipboard -Value -"],
                    input=enc,
                    check=True,
                )
                return True
            except Exception:
                pass
        else:
            # Linux: prefer xclip/xsel on X11, wl-copy on Wayland
            session = os.environ.get("XDG_SESSION_TYPE", "").lower()
            if session == "x11":
                backends = [
                    ("xclip", ["xclip", "-selection", "clipboard"]),
                    ("xsel", ["xsel", "--clipboard", "--input"]),
                    ("wl-copy", ["wl-copy"]),
                ]
            else:
                backends = [
                    ("wl-copy", ["wl-copy"]),
                    ("xclip", ["xclip", "-selection", "clipboard"]),
                    ("xsel", ["xsel", "--clipboard", "--input"]),
                ]

            for name, cmd in backends:
                if shutil.which(name):
                    try:
                        subprocess.run(cmd, input=enc, check=True)
                        return True
                    except Exception:
                        continue

        return False

    used_clip = set_clipboard_with_fallback(txt)

    # choose paste hotkey based on platform
    if sys.platform.startswith("darwin"):
        paste_keys = ("command", "v")
    else:
        paste_keys = ("ctrl", "v")

    if used_clip:
        time.sleep(0.12)
        try:
            pyautogui.hotkey(*paste_keys)
        except Exception:
            try:
                pyautogui.keyDown("shift")
                pyautogui.press("insert")
                pyautogui.keyUp("shift")
            except Exception:
                pyautogui.write(txt)
    else:
        pyautogui.write(txt)
