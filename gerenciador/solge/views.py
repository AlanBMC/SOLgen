from django.shortcuts import render, redirect
import pdfplumber
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import time
import pyperclip
import json
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def cria_sessao_produtos(request):
    data_sessao = request.session.get('produtos', [])
    if request.method == 'POST':
        arquivo = request.FILES.get('arquivo')
        data = extrai_dados_xml(arquivo)
        request.session['produtos'] = data
        if not data_sessao:
            data_sessao = data
        return render(request, 'tabela.html', {'produtos': data_sessao})
    else:
        return render(request, 'tabela.html', {'produtos': data_sessao})

def atualiza_produtos(request):
    if request.method == 'POST':
        try:
            # Receber os dados enviados via AJAX
            dados = json.loads(request.body)
            codigo_de_barras = dados.get('codigo_de_barras')
            nome = dados.get('nome')
            valor_revenda = dados.get('valor_revenda')

            # Atualizar a sessão com os novos dados
            produtos = request.session.get('produtos', [])
            for produto in produtos:
                if produto['codigo_de_barras'] == codigo_de_barras:
                    produto['nome'] = nome
                    produto['valor_revenda'] = valor_revenda
                    break

            # Salvar a sessão com os novos valores
            request.session['produtos'] = produtos
            request.session.modified = True

            return JsonResponse({'status': 'success', 'message': 'Produto atualizado na sessão'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Método inválido'})

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

def tratamento_de_quantidade_valor_un(vProd, qCom):
    """
    tratamento de quantidade, recebe o valor total da mercadoria, a quantidade e o tipo de quantidade
    """
    #podemos fazer outros tipos de tratamento.
    valor_unitario = vProd/ (qCom*12)

    return valor_unitario



def envia_pro_pyautogui(request):

    produtos = request.session.get('produtos', [])
    print(produtos)
    return redirect('criasessao')