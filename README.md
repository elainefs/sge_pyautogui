<div align="center">
    <h1>Automação de cadastro Web com PyAutoGUI</h1>
    <img src="https://img.shields.io/github/repo-size/elainefs/sge_pyautogui">
    <img src="https://img.shields.io/github/languages/top/elainefs/sge_pyautogui"> 
    <img src="https://img.shields.io/github/last-commit/elainefs/sge_pyautogui?color=blue">
    <img src="https://img.shields.io/github/license/elainefs/sge_pyautogui.svg?color=blue">
    <br><br>
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/Pandas-130654?style=flat&logo=pandas&logoColor=white">
</div>

## 📘 Sobre

Este projeto consiste em uma automação de interface (RPA) desenvolvida para realizar o cadastro em massa de itens em um [sistema web de gerenciamento de estoque](https://django-sge.onrender.com) desenvolvido por mim. O script lê dados de múltiplos arquivos CSV e simula a interação humana com o navegador.

O fluxo do projeto funciona da seguinte forma:

**Leitura de Dados**: O script processa 6 arquivos CSV localizados na pasta `database` utilizando a biblioteca Pandas.

**Interação com a UI**: Através do PyAutoGUI, a automação controla o mouse e o teclado para navegar pelo sistema.

**Tratamento de Caracteres Especiais**: Para evitar erros de codificação (encoding) em campos de texto, o projeto utiliza um script auxiliar (`clipboard.py`) que gerencia o comando copiar/colar (clipboard), garantindo a integridade dos dados inseridos, independente do sistema operacional.

## 🎥 Demonstração

<details>
<summary>Clique para visualizar a automação em execução</summary>
 <video width="520" height="340" controls>
  <source src="video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video> 
</details>

## 🛠️ Tecnologias

- Python 3.12
- Pandas 2.3
- PyAutoGUI 0.9

## 💻️ Scripts:

`automation.py`: Script principal com a lógica de loop e cadastro.

`position.py`: Utilitário para capturar as coordenadas (x, y) do mouse em tempo real.

`clipboard.py`: Módulo responsável por detectar o encoding dos arquivos e realizar a função de "colar" textos, resolvendo o problema de caracteres especiais.

## ⚙️ Como usar

Siga os passos abaixo para configurar e executar a automação:

1. Clone o repositório

```bash
git clone https://github.com/elainefs/sge_pyautogui.git
```

2. Crie e ative um ambiente virtual

```bash
python3 -m venv .venv # Para Windows use: python -m venv .venv

source .venv/bin/activate  # Para Windows use: .venv\Scripts\activate
```

3. Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

4. Mapeamento de Coordenadas

Como sistemas web variam de acordo com a resolução da tela, você deve primeiro identificar onde o script deve clicar:

Execute o script auxiliar:

```bash
python3 position.py # ou python position.py
```

Posicione o mouse sobre os campos e botões do sistema e anote as coordenadas exibidas no terminal.

Atualize as coordenadas no arquivo `automation.py` conforme necessário.

5. Execução

Com as coordenadas configuradas e os arquivos na pasta database, basta iniciar o script principal:

```bash
python automation.py
```

> [!TIP]
> O PyAutoGUI possui um recurso de "failsafe". Se algo der errado, mova o mouse rapidamente para o canto superior esquerdo da tela para interromper a execução do script imediatamente.

## 📄 Licença

Este projeto está sobre a licença MIT. Veja o arquivo [LICENSE](https://github.com/elainefs/sge_pyautogui/blob/main/LICENSE) para mais informações.

---

Made with ❤️ by [Elaine Ferreira](https://github.com/elainefs)
