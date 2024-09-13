import json
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import pdfplumber

def abre_base_de_dados_json():
    data = []  # Inicializa uma lista vazia para armazenar os dados
    try:
        with open('C:/Users/alanb/OneDrive/Área de Trabalho/SOLgen/SOLgen/src/json/dados_extraidos.json', encoding='utf-8') as data_json:
            data = json.load(data_json)
            return data
    except FileNotFoundError:
        return print("Arquivo 'dados_extraidos.json' não encontrado. Verifique o caminho e tente novamente.")

    except json.JSONDecodeError:
        return print("Erro ao decodificar o arquivo JSON. Verifique se o arquivo está no formato correto.")
    return data



def adiciciona_produtos_json(dados_novos):
    data_atual = abre_base_de_dados_json()
    # Adiciona o novo produto à lista existente
    data_atual.append(dados_novos)
    with open('C:/Users/alanb/OneDrive/Área de Trabalho/SOLgen/SOLgen/src/json/dados_extraidos2.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_atual, json_file, ensure_ascii=False, indent=4)



def abre_explorador_de_arquivo_apenas_xml():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    arquivo_selecionado = filedialog.askopenfilename(
        title='Selecioine o arquivo XML',
        filetypes=(('Arquivo XML', '*.xml'), ('Todos os arquivos', '*.*'))
    )
    if arquivo_selecionado:
        print(f'arquivo selecionado: {arquivo_selecionado}')
        return arquivo_selecionado
    else:
        print('Nenhum arquivo selecionado')

def tratamento_de_quantidade_valor_un(vProd, qCom):
    """
    tratamento de quantidade, recebe o valor total da mercadoria, a quantidade e o tipo de quantidade
    """
    #podemos fazer outros tipos de tratamento.
    valor_unitario = vProd/ (qCom*12)

    return valor_unitario


def  extrai_dados_xml():
    arquivo_xml = abre_explorador_de_arquivo_apenas_xml()
    data = []
    try:
        tree = ET.parse(arquivo_xml)  # Carrega a árvore XML
        root = tree.getroot()  # Obtém o elemento raiz do XML
        codigo_de_barras = ''
        ncm = ''
        nome_produto = ''
        cfop = ''
        unidade_comercial = ''
        quantidade_comercial = ''
        valor_unitario_comercial = ''
        valor_total = ''
        # Percorrer todas as tags e seus textos
        for elem in root.iter():
            tag = elem.tag.replace('{http://www.portalfiscal.inf.br/nfe}', '')
            if tag == 'cEAN':
                codigo_de_barras = elem.text
            elif tag == 'NCM':
                ncm = elem.text
            elif tag == 'xProd':
                nome_produto = elem.text
            elif tag == 'CFOP':
                cfop = elem.text
            elif tag == 'uCom':
                unidade_comercial =  elem.text
            elif tag == 'qCom':
                quantidade_comercial = elem.text
            elif tag == 'vUnCom':
                valor_unitario_comercial = elem.text
            elif tag == 'vProd':
                valor_total = elem.text
            elif tag == 'uTrib':
                utrib = elem.text
                if utrib == 'DZ':
                    valor_unitario_comercial = tratamento_de_quantidade_valor_un(valor_total, quantidade_comercial)
                
            if nome_produto and codigo_de_barras and valor_total and valor_unitario_comercial and ncm and cfop:
                dicio = {
                    'nome': nome_produto,
                    'codigo_de_barras': codigo_de_barras,
                    'ncm': ncm,
                    'cfop': cfop,
                    'unidade_comercial': unidade_comercial,
                    'quantidade_comercial': quantidade_comercial,
                    'valor_unitario_comercial': valor_unitario_comercial,
                    'valor_revenda':valor_unitario_comercial,
                    'valor_total': valor_total
                }
                data.append(dicio)
                codigo_de_barras = ''
                ncm = ''
                nome_produto = ''
                cfop = ''
                unidade_comercial = ''
                quantidade_comercial = ''
                valor_unitario_comercial = ''
                valor_total = ''
        return data
    except ET.ParseError as e:
        print(f'O erro foi devido ao {e}')



def abre_explorador_para_pdf():
    """
    Função para abrir o explorador de arquivos e selecionar um arquivo PDF.
    
    :return: O caminho do arquivo PDF selecionado ou None se nenhum arquivo for selecionado.
    """
    # Inicializa o Tkinter e esconde a janela principal
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do tkinter

    # Garante que a janela de diálogo apareça na frente
    root.attributes('-topmost', True)

    # Abre a janela de seleção de arquivos, permitindo apenas arquivos PDF
    arquivo_pdf = filedialog.askopenfilename(
        title='Selecione um arquivo PDF',
        filetypes=(('Arquivos PDF', '*.pdf'), ('Todos os arquivos', '*.*'))
    )

    # Fecha a janela tkinter
    root.destroy()

    # Retorna o caminho do arquivo selecionado, ou None se nenhum arquivo for selecionado
    if arquivo_pdf:
        print(f'Arquivo PDF selecionado: {arquivo_pdf}')
        return arquivo_pdf
    else:
        print('Nenhum arquivo selecionado.')
        return None
    


def atualiza_dados():
    dados = []
    arquivo_pdf = abre_explorador_para_pdf()
    with pdfplumber.open(arquivo_pdf) as pdf:
        for page in pdf.pages:
            tabelas = page.extract_tables()
            for tabela in tabelas:
                # Para cada linha da tabela, filtra elementos vazios
                tabela_filtrada = [[item for item in linha if item] for linha in tabela]
                
                # Filtra as listas vazias resultantes
                tabela_filtrada = [linha for linha in tabela_filtrada if linha]
                if len(tabela_filtrada) <= 3:
                    nome = tabela_filtrada[0][0][5:]
                    codigo =  tabela_filtrada[1][0] # Exemplo de uso
                    preco = tabela_filtrada[2][0]
                                    
                    item = {
                        "nome": nome,
                        "codigo": codigo,
                        "preco": preco
                    }
                    dados.append(item)
                elif len(tabela_filtrada) >3:
                    nome = tabela_filtrada[0][0][5:] + tabela_filtrada[1][0]
                    codigo =  tabela_filtrada[2][0] # Exemplo de uso
                    preco = tabela_filtrada[3][0]
                    item = {
                        "nome": nome,
                        "codigo": codigo,
                        "preco": preco
                    }
                    dados.append(item)
# Exemplo de uso

                           
    with open('C:/Users/alanb/OneDrive/Área de Trabalho/SOLgen/SOLgen/src/json/dados_extraidos2.json', 'w', encoding='utf-8') as json_file:
        json.dump(dados, json_file, ensure_ascii=False, indent=4)

    # Exibe os dados salvos para confirmação


