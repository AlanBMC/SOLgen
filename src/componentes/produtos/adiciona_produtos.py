import json
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET

def  abre_base_de_dados_json():
    try:
        with open('dados_extraidos.json', encoding='utf-8') as data_json:
            data = json.load(data_json)

    except FileNotFoundError:
        data = []
        print("Arquivo 'dados_extracao.json' não encontrado. Verifique o caminho e tente novamente.")

def adiciciona_produtos_json(dados_novos, data_json):
    
    with open('dados teste insercao.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_json, json_file, ensure_ascii=False, indent=4)




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


