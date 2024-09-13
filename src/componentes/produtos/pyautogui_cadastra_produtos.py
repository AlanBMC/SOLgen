import pyautogui
import pyperclip
import time

def digita_texto(texto):
    time.sleep(0.5)
    pyautogui.write(texto, interval=0.05) 
    

def cola_texto(texto):
    """
    Função para colar texto usando pyperclip e pyautogui.
    
    :param texto: String a ser colada.
    """
    pyperclip.copy(texto)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    
#pyautogui.typewrite(texto) # Digita o texto na tela
def clica_ok():
    pass

def clica_fiscal():
    pass

def clica_cfop(cfop):

    digita_texto(cfop)
    pass

def clica_ncm(ncm):
    digita_texto(ncm)
    pass

def clica_nome(nome):
    cola_texto(nome)
    pass

def clica_preco(preco):
    cola_texto(preco)
    pass

def clica_preco_compra(preco_un):
    
    cola_texto(preco_un)
    pass

def clica_salvar():
    pass