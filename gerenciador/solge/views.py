from django.shortcuts import render, redirect
import pdfplumber
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import time
import pyperclip
import pyautogui
import json
import math
from pywinauto import Application
from .models import Produto
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect

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

def ajusta_valores_produtos(request):
    if request.method == 'POST':
        porcentagem = float(request.POST.get('porcentagem', 1))  # Padrão para 1, se não fornecido
        
        # Verifica se 'valor-adicional' está vazio e define como 0 se necessário
        valor_adicional_str = request.POST.get('valor-adicional', '')
        adicional = float(valor_adicional_str) if valor_adicional_str else 0  # Usa 0 se o campo estiver vazio

        meia_nota = request.POST.get('meia-nota')  # Aqui você pode usar para outras lógicas, se necessário
        produtos_sessao_cadastro = request.session.get('produtos', [])
            
        for produto in produtos_sessao_cadastro:
            try:
                if meia_nota:
                # Converte 'valor_revenda' para float antes de realizar o cálculo
                    valor_revenda = float(produto['valor_revenda']) * 2
                else:
                    valor_revenda = float(produto['valor_revenda'])
                # Calcula o novo valor revenda
                novo_valor = (valor_revenda * porcentagem) + adicional
                produto['valor_revenda'] = math.ceil(novo_valor)  # Atualiza o valor revenda
            except ValueError:
                # Se não puder converter, pode adicionar lógica para tratar o erro
                return HttpResponse('Erro: Valor revenda inválido')

        request.session['produtos'] = produtos_sessao_cadastro
        return HttpResponseRedirect('atualiza_produtos/')


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
    request.session['produtos'] = []
    return redirect('criasessao')

def atualiza_banco_view(request):
    if request.method == 'POST':
        arquivo  = request.FILES.get('arquivo')
        dados = atualiza_banco(arquivo)
        if Produto.objects.exists():
            Produto.objects.all().delete()

        for valores in dados:
            Produto.objects.create(nome = valores['nome'],
                                   preco = valores['preco'],
                                   codigo_de_barras = valores['codigo'])
            
        return render(request,'atualizando_banco.html')
    else:
        return render(request, 'atualizando_banco.html')
    
def atualiza_banco(arquivo_pdf):
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
                    preco = tabela_filtrada[2][0][3:]
                    preco = float(preco.replace(',', '.'))
                    item = {
                        "nome": nome,
                        "codigo": codigo,
                        "preco": preco
                    }
                    dados.append(item)
                elif len(tabela_filtrada) >3:
                    nome = tabela_filtrada[0][0][5:] + tabela_filtrada[1][0]
                    codigo =  tabela_filtrada[2][0] # Exemplo de uso
                    preco = tabela_filtrada[3][0][3:]
                    preco = float(preco.replace(',', '.'))
                    item = {
                        "nome": nome,
                        "codigo": codigo,
                        "preco": preco
                    }
                    
                    dados.append(item)
    return dados


def impressora(request):
    cards_sessao = request.session.get('cards', [])
    if cards_sessao:
    # Recuperar os produtos correspondentes a esses códigos
        produtos = Produto.objects.filter(codigo_de_barras__in=cards_sessao)
        print(produtos)
        return render(request, 'impressora.html', {'produtos': produtos})
    else:
        return render(request, 'impressora.html')
def adiciona_card(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        codigo_do_produto = body.get('codigo')
        
        try:
            produto = Produto.objects.get(codigo_de_barras=codigo_do_produto)
            
            # Obter os produtos armazenados na sessão (apenas códigos de barra)
            produtos_sessao = request.session.get('cards', [])
            
            # Verificar se o produto já está na sessão
            if codigo_do_produto in produtos_sessao:
                return JsonResponse({'Status': 'Produto já adicionado'}, status=400)
            
            # Adicionar o produto à sessão (somente código de barras)
            produtos_sessao.append(codigo_do_produto)
            request.session['cards'] = produtos_sessao  # Salva a sessão
            
            # Retorna os dados do produto para o front-end
            return JsonResponse({'nome': produto.nome, 'preco': produto.preco, 'codigo': produto.codigo_de_barras})
        
        except Produto.DoesNotExist:
            return JsonResponse({'Status': 'Produto não existe'}, status=404)
    
    return JsonResponse({'erro': 'método incorreto'}, status=405)

def delete_card_impressora(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        produtos_sessao = request.session.get('cards', [])
        if codigo in produtos_sessao:
            produtos_sessao.remove(codigo)
            request.session['cards'] = produtos_sessao
        return redirect('impressora')
def limpa_impressora(request):
    """
    funcao para tirar os cards da sessao
    """
    request.session['cards'] = []
    return redirect('impressora')
    
def chama_fun_automacao_impressora(request):
    etiqueta = 0
    if request.method == 'POST':
        etiqueta_amarela =  request.POST.get('tipo1')
        etiqueta_branca = request.POST.get('tipo2')
        if etiqueta_amarela:
            etiqueta = 1
        elif etiqueta_branca:
            etiqueta = 2
        cards_sessao = request.session.get('cards', [])
        
        # Recuperar os produtos correspondentes a esses códigos
        produtos = Produto.objects.filter(codigo_de_barras__in=cards_sessao)
        
        # Imprimir ou processar os produtos recuperados
        print('etiqueta : ',etiqueta)
        abriu = selecao_tipo_etiqueta(request,etiqueta)
        if abriu:
           if  automacao_pyautogui_impressora(request, produtos):
               
               pass

        request.session['cards'] = []
        return redirect('impressora')
    else:
        return redirect('impressora')



def abrir_bartender_com_arquivo(caminho_bartender, caminho_arquivo_btw):
    """Verifica se o BarTender já está aberto, caso contrário, abre e carrega diretamente o arquivo .btw."""
    try:
        # Tenta conectar-se ao BarTender já aberto
        app = None
        try:
            # Tenta conectar-se ao BarTender em execução
            app = Application(backend="uia").connect(path=caminho_bartender)
            window = app.top_window()
            # Traz a janela para o foco e maximiza
            window.set_focus()
            window.maximize()
            print("BarTender já estava em execução e foi trazido para o foco.")
            return True
        except Exception as e:
            print("BarTender não estava em execução, iniciando...")

        # Se não conseguir conectar, inicia o BarTender
        if app is None:
            app = Application(backend="uia").start(f'"{caminho_bartender}" "{caminho_arquivo_btw}"')
            time.sleep(15)  # Esperar o BarTender carregar completamente

        # Obter a janela principal do BarTender
        window = app.top_window()

        # Traz a janela para o foco e maximiza (caso ainda não tenha sido feita)
        window.set_focus()
        window.maximize()
        print(f"BarTender iniciado com o arquivo {caminho_arquivo_btw}.")
        
        return True
    except Exception as e:
        print(f"Erro ao iniciar ou conectar ao BarTender com o arquivo: {e}")
        return None
def selecao_tipo_etiqueta(request,tipo_etiqueta):
    caminho_bartender = r"C:/Program Files/Seagull/BarTender 2022/BarTend.exe"
    print(tipo_etiqueta, 'etiqueta selecionada em definindo_etiqueta')

    # Definindo o caminho correto baseado no tipo de etiqueta
    if tipo_etiqueta == 1:
        caminho_arquivo_btw = fr"C:/Users/alanb/OneDrive/Área de Trabalho/ETIQUETA AMARELA.btw"
    elif tipo_etiqueta == 2:
        caminho_arquivo_btw = fr"C:/Users/alanb/OneDrive/Área de Trabalho/etiqueta branca.btw"
    else:
        print("Tipo de etiqueta inválido. Selecione 1 ou 2.")
        return None

    # Abrir o BarTender e carregar o arquivo .btw
    window = abrir_bartender_com_arquivo(caminho_bartender, caminho_arquivo_btw)

    # Verifica se o BarTender foi iniciado corretamente
    if window is None:
        print("Falha ao iniciar o BarTender.")
        return None
    else:
        return True

def apaga_texto():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

def enter_text(text):
    pyperclip.copy(text)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

def automacao_pyautogui_impressora(request, produtos):
    for produto in produtos:
        print(produto.nome, produto.preco, produto.codigo_de_barras)
        #etiqueta amarela
        time.sleep(1)
        pyautogui.click(x = 665, y = 294)
        time.sleep(2)
        pyautogui.click(x = 665, y = 294) # posicao do nome
        apaga_texto()
        #escreve
        enter_text(produto.nome)
        time.sleep(1)
        pyautogui.click(x = 642, y = 409)#preço
        apaga_texto()
        #escreve
        enter_text(f'R$ - {produto.preco:.2f}')
        pyautogui.doubleClick(x = 702, y = 554)#codigo de barras
        time.sleep(2)
        pyautogui.click(x = 794, y = 286) # segunda tela do codigo de barras
        apaga_texto()
        #escreve
        enter_text(produto.codigo_de_barras)
        time.sleep(1)
        pyautogui.click(x = 925, y = 687)#botao fechar da segunda janela do codigo de barras
        time.sleep(2)
        pyautogui.click(x = 1109, y = 226) #espaço fora dos campos texto para ter um press
        pyautogui.hotkey('ctrl', 'p')
        time.sleep(4)
        pyautogui.click(x = 681, y = 375) # quantidade
        apaga_texto()
        enter_text('1') #coloca quantidade
        
        pyautogui.click(x = 596, y = 583) # botao imprime
    request.session['cards'] = []
    return True