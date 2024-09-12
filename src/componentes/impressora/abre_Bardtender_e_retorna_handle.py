import time
from pywinauto import Application
import win32gui

def abrir_bartender_com_arquivo(caminho_bartender, caminho_arquivo_btw):
    """Abre o BarTender e carrega diretamente o arquivo .btw."""
    try:
        # Inicia o BarTender com o arquivo .btw como argumento
        app = Application(backend="uia").start(f'"{caminho_bartender}" "{caminho_arquivo_btw}"')
        time.sleep(20)  # Esperar o BarTender carregar completamente
        print(f"BarTender iniciado com o arquivo {caminho_arquivo_btw}.")
        return app
    except Exception as e:
        print(f"Erro ao iniciar o BarTender com o arquivo: {e}")
        return None

def encontrar_handle_janela(app):
    """Encontra o handle da janela do BarTender."""
    try:
        # Acessa a janela principal do BarTender
        janela_principal = app.top_window()
        hwnd = janela_principal.handle
        print(f"Handle da janela principal do BarTender: {hwnd}")
        return hwnd
    except Exception as e:
        print(f"Erro ao encontrar o handle da janela: {e}")
        return None
    

def obter_handle_elemento_pane(app):
    """Obtém o handle do elemento com AutomationId 59648 e ControlType Pane."""
    try:
        # Localiza a janela principal do BarTender
        janela_principal = app.top_window()

        # Localiza o elemento com AutomationId e ControlType
        elemento = janela_principal.child_window(class_name="AfxFrameOrView140u", control_type="Pane").wrapper_object()

        # Obtém o handle do elemento
        handle_elemento = elemento.handle
        print(f"Handle do elemento encontrado: {handle_elemento}")
        return handle_elemento
    except Exception as e:
        print(f"Erro ao obter o handle do elemento: {e}")
        return None
    
    
def definindo_etiqueta(tipo_etiqueta):
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
    app = abrir_bartender_com_arquivo(caminho_bartender, caminho_arquivo_btw)

    # Verifica se o BarTender foi iniciado corretamente
    if app is None:
        print("Falha ao iniciar o BarTender.")
        return None

    # Tentativa de obter os dois handles
    try:
        handle = encontrar_handle_janela(app)
        handle2 = obter_handle_elemento_pane(app)
        
        if handle is None or handle2 is None:
            print("Falha ao encontrar um dos handles.")
            return None
        
        return handle, handle2
    except Exception as e:
        print(f"Erro ao encontrar handles: {e}")
        return None
