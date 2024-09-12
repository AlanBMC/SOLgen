import win32gui
import win32con
import ctypes
import time
from componentes.impressora.abre_Bardtender_e_retorna_handle import *
from componentes.impressora.simulador_teclas import *
from componentes.impressora.win_codigo import *
from componentes.impressora.manda_imprimir import *

# Definir as teclas que vamos simular
TAB = win32con.VK_TAB
ENTER = win32con.VK_RETURN
CTRL = win32con.VK_CONTROL
P = 0x50
PostMessage = ctypes.windll.user32.PostMessageW
BOLEANO = True
# Variável global para armazenar o handle da janela principal
hwnd_global = None
hwnd_global2 = None
def inicializar_bartender(tipo_etiqueta):
    """Inicializa o BarTender e armazena os handles globalmente."""
    global hwnd_global, hwnd_global2
    if hwnd_global is None or hwnd_global2 is None:
        # Inicializa o BarTender e obtém os dois handles
        result = definindo_etiqueta(tipo_etiqueta)
        if result is None:
            print("Erro ao inicializar o BarTender ou encontrar os handles.")
            return None, None
        
        hwnd_global, hwnd_global2 = result
        print(f"Handles inicializados: {hwnd_global}, {hwnd_global2}")
    
    return hwnd_global, hwnd_global2


def envia_para_impressora(produtos, tipo_etiqueta, quantidade):
    """Envia os produtos para a impressora."""
    for produto in produtos:
        nome = produto['nome'][:30]
        nome = nome.replace('\n', ' ')
        print(nome)
        preco =  produto['preco']
        codigo = produto['codigo']
        print(tipo_etiqueta, quantidade)
        print('imprimindo')
        comunicacao_com_impressora(nome, preco, codigo, tipo_etiqueta, quantidade)
    print('Processo finalizado')

def focar_janela(hwnd):
    """Coloca a janela em foco."""
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.5)

def pressiona_tecla(hwnd, key):
    """Pressiona uma tecla."""
    PostMessage(hwnd, win32con.WM_KEYDOWN, key, 0)

def solta_tecla(hwnd, key):
    """Solta uma tecla."""
    PostMessage(hwnd, win32con.WM_KEYUP, key, 0)

def inserindo_texto(hwnd, text):
    """Insere texto caractere por caractere na janela."""
  
    limpa(hwnd)
    time.sleep(0.5)
    for char in text:
        time.sleep(0.05)  # Pequeno atraso para simular a digitação
        PostMessage(hwnd, win32con.WM_CHAR, ord(char), 0)


    
def abre_janela_imprimir(quantidade):
    """Abre a janela de impressão."""
    hwnd = hwnd_global  # Usa o handle global
    hwnd_quantidade = 134860
    hwnd_janela_imprimir = 265670  # Caso necessário
    pressiona_tecla(hwnd, CTRL)
    pressiona_tecla(hwnd, P)
    time.sleep(1)
    solta_tecla(hwnd, CTRL)
    solta_tecla(hwnd, P)
    inserindo_texto(hwnd_quantidade, quantidade)
    pressiona_tecla(1445676, ENTER)
    solta_tecla(1445676, ENTER)

def comunicacao_com_impressora(nome, preco, codigo, tipo_etiqueta, quantidade):
    """Realiza a comunicação com a impressora usando dois handles."""
    hwnd, handle2 = inicializar_bartender(tipo_etiqueta)
    if hwnd is None or handle2 is None:
        print("Handles não encontrados. Falha ao se comunicar com a impressora.")
        return

    # Use o handle principal para navegação com TAB e ENTER
    pressiona_tecla(hwnd, TAB)
    time.sleep(0.1)
    solta_tecla(hwnd, TAB)
    time.sleep(0.5)
    
    # Pressione ENTER usando o handle do 'Pane'
    pressiona_tecla(handle2, ENTER)
    time.sleep(0.1)
    solta_tecla(handle2, ENTER)
    time.sleep(0.5)

    # Insere o nome usando o handle do 'Pane'
    
    inserindo_texto(handle2, nome)
    pressiona_tecla(handle2, ENTER)
    time.sleep(0.1)
    solta_tecla(handle2, ENTER)

    # Segunda etapa - Insere o preço
    pressiona_tecla(hwnd, TAB)
    time.sleep(0.1)
    solta_tecla(hwnd, TAB)
    time.sleep(0.5)
    pressiona_tecla(handle2, ENTER)
    time.sleep(0.1)
    solta_tecla(handle2, ENTER)
    time.sleep(0.5)
    inserindo_texto(handle2, preco)
    pressiona_tecla(handle2, ENTER)

    # Terceira etapa - Insere o código
    pressiona_tecla(hwnd, TAB)
    time.sleep(0.1)
    solta_tecla(hwnd, TAB)
    time.sleep(0.5)
    pressiona_tecla(handle2, ENTER)
    time.sleep(0.1)
    solta_tecla(handle2, ENTER)
    time.sleep(0.5)
    #edita
    handle_codigo =handle_campo_codigo()
    inserindo_texto(handle_codigo, codigo)
    handle_janela_principal, titulo_da_janela_principal = get_main_window_handle_and_title()
    clicar_botao_ok(handle_janela_principal)
    
    clicar_botao_imprimir(str(quantidade))