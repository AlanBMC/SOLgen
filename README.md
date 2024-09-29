# Gerenciador para Sistemas PDV's Legados - SOLgen (Versão 3.0.0)

Este projeto é um **Gerenciador para Sistemas PDV's Legados**, focado na automação de processos de cadastro de produtos, extração de dados de arquivos XML e PDF, e geração de etiquetas utilizando automação e integração com leitores de código de barras. O sistema é voltado para simplificar o processo de gestão em PDV's legados e tornar o fluxo de trabalho mais ágil e automatizado.

## Funcionalidades

- **Automação de Cadastramento**: Cadastra produtos automaticamente em sistemas PDV's legados usando automação com a biblioteca `pyautogui`.
- **Extração de Dados**: Extração de dados importantes de arquivos XML e PDF, permitindo geração de relatórios e integração com sistemas de cadastro.
- **Integração com Leitores de Código de Barras**: Permite a bipagem de códigos de barras para automação e geração de etiquetas.
- **Impressão de Etiquetas**: Integração com o software **Bartend** para geração de etiquetas de produtos para impressão.

## Tecnologias Utilizadas

### Bibliotecas

- **pyautogui**: Utilizada para automação de eventos de teclado e mouse.
- **xml.etree.ElementTree**: Para extração e manipulação de dados de arquivos XML.
- **pdfplumber**: Utilizada para extração de texto e tabelas de arquivos PDF.
- **pywinauto**: Para automação de interfaces gráficas e controle de janelas de sistemas legados.
- **pywin32**: Para manipulação direta de APIs do Windows.
- **ctypes**: Para integração com bibliotecas de baixo nível.
- **flet**: Framework para construção da interface gráfica.

### Frameworks e Ferramentas

![Flet](https://img.shields.io/badge/Flet-cd2152?style=plastic&logo=flutter&logoColor=white)
![Python](https://img.shields.io/badge/Python-D7CB25?style=plastic&logo=python&logoColor=blue)

## Requisitos

- **Bartend**: Necessário para gerar e imprimir etiquetas.
- **Python 3.x**: Certifique-se de que o Python está instalado.
- **Dependências do Projeto**: Todas as bibliotecas listadas nas dependências.

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/usuario/repositorio.git
    cd repositorio
    ```

2. Instale as dependências do projeto:

    ```bash
    pip install pyautogui pdfplumber pywin32 pywinauto ctypes flet pygame gTTS
    ```

3. Certifique-se de que o **Bartend** está instalado corretamente no sistema. Você também deve ajustar o caminho para o Bartend e o modelo de etiquetas no código.

## Como Usar

1. Inicie o sistema com o seguinte comando:

    ```bash
    python main.py
    ```

2. A interface gráfica permite realizar as seguintes tarefas:
   - **Cadastro Automático de Produtos**: Cadastrar produtos em sistemas legados usando automação.
   - **Extração de Dados**: Extrair dados relevantes de arquivos XML e PDF.
   - **Bipagem e Impressão de Etiquetas**: Ler códigos de barras e gerar etiquetas para impressão no Bartend.

## Planejamento da Versão 3.0.0

Na versão 3.0.0, o projeto trará diversas melhorias e novas funcionalidades, como:
- **Otimização da Automação**: Melhorias no fluxo de automação para reduzir tempo e erros em sistemas PDV's.
- **API RESTful**: Implementação de uma API para permitir integração remota de sistemas externos com o SOLgen.
- **Interface Mais Amigável**: Melhorias na interface gráfica usando o framework Flet.
- **Suporte para Novos Formatos de Arquivos**: Expansão do suporte para outros formatos de arquivos, além de XML e PDF.

## Contribuição

Contribuições são sempre bem-vindas! Se você quiser contribuir com o projeto, sinta-se à vontade para abrir issues e pull requests.

---

**Adendo para a Versão 3.0.0**: 
Estamos planejando uma atualização significativa com novas funcionalidades e melhorias na usabilidade, na eficiência da automação e integração de APIs. Fique atento para as novidades!

## Sobre o autor


|  |  |
|:-------------:|:------------------------------------------------------------:|
|  <img src="alan.jpeg" width="150px"></br> **Alan Bruno Morais Costa** | 
Me chamo Alan, sou estudante de Ciências da Computação na Universidade Federal de Mato Grosso (UFMT). Este repositório contém o projeto prático para cadastramento de produtos e impressao de etiquetas para um estabelecimento local. irei sempre tentar trazer uma melhor versão com funcoes mais dinamicas, mais ampla e com um designer agradavel. Atualmente este projeto é um protótipo afim de facilidar as tarefas diarias de impressão e cadastramento de produtos.  |

- **Email:** alanbrunomoraescosta18@hotmail.com
- **LinkedIn:** [Alan  LinkedIn](https://www.linkedin.com/in/alan-morais-4861322b0)
