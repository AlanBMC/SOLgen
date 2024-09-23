from django.shortcuts import render, redirect
import pdfplumber
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import time
import pyperclip
# Create your views here.
def home(request):
    return render(request, 'home.html')




def atualiza_data_base():
    """
    pega o arquivo PDF de etiquetas
    esxtrai os dados e salva no banco

    """
    

def impressora():
    """
    Compara os codigos recebidos com os do banco de dados
    prepara os codigos achados
    imprime os codigos achados

    """

def cadastro_produto(request):
    """
    Recebe um arquivo XML ou PDF, extrai dados do XML, salva os dados no banco,
    envia os dados para uma função que interage com o PyAutoGUI, e cria uma
    sessão com os produtos.
    """
    if request.method == 'POST':
        arquivo = request.FILES.get('arquivo')
        data = extrai_dados_xml(arquivo)
        data_sessao = request.session.get('produtos', [])

        if not data_sessao:
            request.session['produtos'] = data
            data_sessao = data

        return render(request, 'tabela.html', {'produtos': data_sessao})
    else:
        return render(request, 'tabela.html')

def atualiza_dados_da_sessao(request):
    pass

def cadastra_produto_pyautogui(request):
    if request.method == 'POST':
        data = request.session.get('produtos', [])
        if data:
            print(data)  # Para fins de debug
            for produto in data:
                try:
                    pyautogui2(produto['nome'], produto['codigo_de_barras'], produto['ncm'], produto['valor_revenda'])
                except Exception as e:
                    print(f"Erro ao processar produto {produto['nome']}: {e}")

            # Limpar a sessão após o processamento
            request.session.pop('produtos', None)
        
        return redirect('cadastro_produto')
    else:
        return render(request, 'tabela.html')


def extrai_dados(arquivo_pdf):

    dados = []
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


def tratamento_de_quantidade_valor_un(vProd, qCom):
    """
    tratamento de quantidade, recebe o valor total da mercadoria, a quantidade e o tipo de quantidade
    """
    #podemos fazer outros tipos de tratamento.
    valor_unitario = vProd/ (qCom*12)

    return valor_unitario

def  extrai_dados_xml(arquivo_xml):
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

def enter_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)

def digita_texto(texto):
    pyautogui.write(texto, interval=0.1)
    
def click_ok():
    time.sleep(1)
    pyautogui.click(x=1154, y=562)

def pyautogui2(item_nome, item_codigo, item_ncm, item_preco_revenda):
    print('cadastrando')
def pyautogui(item_nome, item_codigo, item_ncm, item_preco_revenda):
    # Novo item
    time.sleep(2)
    pyautogui.click(x=1239, y=185)
    time.sleep(1)
    # Clica em OK
    click_ok()

    # Nome do item
    pyautogui.click(x=715, y=280)
    enter_text(item_nome)
    time.sleep(0.5)

    # Clica na janela de fiscal
    pyautogui.click(x=612, y=307)
    time.sleep(1)

    # Clica no input de NCM
    pyautogui.click(x=729, y=353)
    digita_texto(item_ncm)
    time.sleep(1)
    

    
    # Volta para geral
    pyautogui.click(x=416, y=306)
    time.sleep(1)

    # Coloca o código
    pyautogui.click(x=590, y=334)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    enter_text(item_codigo)
    time.sleep(1)

    # Coloca preço de revenda
    pyautogui.click(x=577, y=592)
    enter_text(item_preco_revenda)
    time.sleep(1)

    # Salva item
    pyautogui.click(x=1460, y=187)
    time.sleep(1)

    # Aperta ok após salvar
    click_ok()
    time.sleep(2)  