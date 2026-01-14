import time

import pandas as pd
import pyautogui

from clipboard import detect_encoding, paste_text

link = "https://django-sge.onrender.com"
user = "adminsge"
password = "adminsge"

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=936, y=464)
pyautogui.write(user)
pyautogui.press("tab")
pyautogui.write(password)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Create Suppliers
pyautogui.click(x=97, y=224)
csv_path_supplier = "database/suppliers.csv"
enc = detect_encoding(csv_path_supplier)
supplier_table = pd.read_csv(csv_path_supplier, encoding=enc)

for row in supplier_table.index:
    time.sleep(1)
    pyautogui.click(x=1815, y=264)
    time.sleep(1)
    pyautogui.click(x=628, y=389)
    paste_text(supplier_table.loc[row, "name"])
    pyautogui.press("tab")
    paste_text(supplier_table.loc[row, "description"])
    pyautogui.press("tab")
    pyautogui.press("enter")

# Create Brands
time.sleep(1)
pyautogui.click(x=64, y=275)
csv_path_brand = "database/brands.csv"
enc = detect_encoding(csv_path_brand)
brand_table = pd.read_csv(csv_path_brand, encoding=enc)

for row in brand_table.index:
    time.sleep(1)
    pyautogui.click(x=1815, y=264)
    time.sleep(1)
    pyautogui.click(x=628, y=389)
    paste_text(brand_table.loc[row, "name"])
    pyautogui.press("tab")
    paste_text(brand_table.loc[row, "description"])
    pyautogui.press("tab")
    pyautogui.press("enter")

# Create Categories
time.sleep(1)
pyautogui.click(x=71, y=326)
csv_path_categories = "database/categories.csv"
enc = detect_encoding(csv_path_categories)
categories_table = pd.read_csv(csv_path_categories, encoding=enc)

for row in categories_table.index:
    time.sleep(1)
    pyautogui.click(x=1815, y=264)
    time.sleep(1)
    pyautogui.click(x=628, y=389)
    paste_text(categories_table.loc[row, "name"])
    pyautogui.press("tab")
    paste_text(categories_table.loc[row, "description"])
    pyautogui.press("tab")
    pyautogui.press("enter")

# Create Products
time.sleep(1)
pyautogui.click(x=58, y=373)
csv_path_products = "database/products.csv"
enc = detect_encoding(csv_path_products)
products_table = pd.read_csv(csv_path_products, encoding=enc)

for row in products_table.index:
    time.sleep(1)
    pyautogui.click(x=1815, y=458)
    time.sleep(1)
    pyautogui.click(x=570, y=390)
    paste_text(products_table.loc[row, "title"])
    pyautogui.press("tab")
    pyautogui.click(x=615, y=468)
    pyautogui.write(str(products_table.loc[row, "category"]))
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.click(x=572, y=544)
    pyautogui.write(str(products_table.loc[row, "brand"]))
    pyautogui.press("enter")
    pyautogui.press("tab")
    paste_text(products_table.loc[row, "description"])
    pyautogui.press("tab")
    paste_text(products_table.loc[row, "serial_number"])
    pyautogui.press("tab")
    paste_text(products_table.loc[row, "purchase_price"])
    pyautogui.press("tab")
    paste_text(products_table.loc[row, "sales_price"])
    pyautogui.press("tab")
    pyautogui.press("enter")

# Create Inflow
time.sleep(1)
pyautogui.click(x=57, y=432)
csv_path_inflows = "database/inflow.csv"
enc = detect_encoding(csv_path_inflows)
inflows_table = pd.read_csv(csv_path_inflows, encoding=enc)

for row in inflows_table.index:
    time.sleep(1)
    pyautogui.click(x=1811, y=259)
    time.sleep(1)
    pyautogui.click(x=603, y=384)
    pyautogui.write(str(inflows_table.loc[row, "supplier"]))
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.click(x=606, y=467)
    pyautogui.write(str(inflows_table.loc[row, "product"]))
    pyautogui.press("enter")
    pyautogui.press("tab")
    paste_text(inflows_table.loc[row, "quantity"])
    pyautogui.press("tab")
    paste_text(inflows_table.loc[row, "description"])
    pyautogui.press("tab")
    pyautogui.press("enter")

# Create outflow
time.sleep(1)
pyautogui.click(x=56, y=478)
csv_path_outflows = "database/outflow.csv"
enc = detect_encoding(csv_path_outflows)
outflows_table = pd.read_csv(csv_path_outflows, encoding=enc)

for row in outflows_table.index:
    time.sleep(1)
    pyautogui.click(x=1835, y=464)
    time.sleep(1)
    pyautogui.click(x=579, y=386)
    pyautogui.write(str(outflows_table.loc[row, "product"]))
    pyautogui.press("enter")
    pyautogui.press("tab")
    paste_text(outflows_table.loc[row, "quantity"])
    pyautogui.press("tab")
    paste_text(outflows_table.loc[row, "description"])
    pyautogui.press("tab")
    pyautogui.press("enter")
