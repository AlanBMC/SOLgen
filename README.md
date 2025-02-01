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

![Django](https://img.shields.io/badge/Django-1cb42f?style=plastic&logo=Django&logoColor=white)
![Python](https://img.shields.io/badge/Python-D7CB25?style=plastic&logo=python&logoColor=blue)

### Motivo da Descontinuação

Durante o desenvolvimento, foi identificado vários desafios estruturais que comprometeram a viabilidade do projeto a longo prazo. Para garantir um sistema mais robusto e escalável, optei por iniciar um novo repositório, com uma abordagem melhor planejada.

O aprendizado obtido com o SOLgen, o prototipo, foi fundamental para guiar, esclarecer sobre o caminho que irei tomar daqui pra frente em relação ao projeto.

## Sobre o autor


|  |  |
|:-------------:|:------------------------------------------------------------:|
|  <img src="alan.jpeg" width="150px"></br> **Alan Bruno Morais Costa** | 
Me chamo Alan, sou estudante de Ciências da Computação na Universidade Federal de Mato Grosso (UFMT). Este repositório contém o projeto prático para cadastramento de produtos e impressao de etiquetas para um estabelecimento local. irei sempre tentar trazer uma melhor versão com funcoes mais dinamicas, mais ampla e com um designer agradavel. Atualmente este projeto é um protótipo afim de facilidar as tarefas diarias de impressão e cadastramento de produtos.  |

- **Email:** alanbrunomoraescosta18@hotmail.com
- **LinkedIn:** [Alan  LinkedIn](https://www.linkedin.com/in/alan-morais-4861322b0)
