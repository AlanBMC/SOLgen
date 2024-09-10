# Gerenciador para Sistemas PDV's Legados - SOLgen

Este projeto é um **Gerenciador para Sistemas PDV's Legados**, que realiza o cadastramento automático de produtos utilizando automação com a biblioteca `pyautogui`, faz a extração de dados de arquivos XML e PDF, e permite a bipagem de códigos de barras para a impressão de etiquetas. Para a impressão, o **Bartend** deve estar instalado na máquina.

## Funcionalidades

- **Cadastramento Automático**: Automação do cadastro de produtos em sistemas PDV's legados utilizando a biblioteca `pyautogui`.
- **Extração de Dados**: Extração de dados relevantes de arquivos XML e PDF para a geração de relatórios e processamento de informações.
- **Bipagem de Códigos de Barras**: Integração com leitor de códigos de barras para impressão de etiquetas.
- **Impressão de Etiquetas**: Integração com o software **Bartend** para gerar e imprimir etiquetas de produtos.

## Tecnologias Utilizadas

### Bibliotecas

- **pyautogui**: Automação do teclado e mouse para interagir com sistemas legados.
- **xml.etree.ElementTree**: Extração de dados de arquivos XML.
- **pdfplumber**: Extração de dados de arquivos PDF.
- **pywinauto**: Manipulação de eventos de teclado e mouse.
- **pywin32**: Interação com a API do Windows.
- **ctypes**: Interface com código C para bibliotecas de baixo nível.
  
### Framework and Ferramentas

![Flet](https://img.shields.io/badge/Flet-cd2152?style=plastic&logo=flutter&logoColor=white)

![Python](https://img.shields.io/badge/Python-D7CB25?style=plastic&logo=python&logoColor=blue)

## Requisitos

- **Bartend**: O software Bartend deve estar instalado para que as etiquetas possam ser impressas.
- **Python 3.x**: Certifique-se de ter o Python instalado.
- As bibliotecas listadas nas dependências abaixo.

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/usuario/repositorio.git
    cd repositorio
    ```

2. Instale as dependências:

    ```bash
    pip install pyautogui pdfplumber pywin32 pywinauto ctypes flet
    ```

3. Certifique-se de que o **Bartend** está instalado corretamente no sistema.

 - Edite o arquivo para o caminho do seu bartender e suas etiquetas.

## Como Usar

1. Execute o sistema com o comando:

    ```bash
    python GUI.py
    ```

2. Utilize a interface gráfica para:
   - Realizar o cadastramento automático de produtos.
   - Extrair dados de arquivos XML e PDF.
   - Bipar códigos de barras para gerar e imprimir etiquetas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar o projeto.


