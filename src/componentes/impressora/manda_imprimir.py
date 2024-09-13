from componentes.impressora.win_codigo import *
import win32gui,win32con
from pywinauto import Application
from componentes.impressora.impressao import *
from componentes.impressora.simulador_teclas import *
import time

def find_imprimir_button_in_pane(parent_handle):
    """Procura o botão 'Imprimir Ctrl+P' dentro do painel 'xtpBarTop'."""
    # Conectar à aplicação já aberta através do handle
    app = Application(backend='uia').connect(handle=parent_handle)

    # Obter a janela pai a partir do handle
    parent_window = app.window(handle=parent_handle)

    # Localizar o painel xtpBarTop
    pane = parent_window.child_window(auto_id="59419", control_type="Pane", class_name="XTPDockBar")
    if pane.exists():
        print("Painel 'xtpBarTop' encontrado.")
        
        return pane.handle
    else:
        print("Painel 'xtpBarTop' não encontrado.")
        return None

def defini_quantidade_de_impressao(parent_handle, text):
    """Procura o campo de edição usando AutomationId e define o valor."""
    automation_id="22006"
    class_name="Edit"
    app = Application(backend='uia').connect(handle=parent_handle)
    parent_window = app.window(handle=parent_handle)

    # Localizar o campo de edição
    edit_field = parent_window.child_window(auto_id=automation_id, control_type="Edit", class_name=class_name)

    if edit_field.exists():
        edit_field.set_text(text)  # Definir o valor do campo de edição
        print(f"Campo de edição encontrado e valor '{text}' definido.")
        return True
    else:
        print("Campo de edição não encontrado.")
        return False


def clicar_botao_imprimir(copias):
    """Procura o botão 'Imprimir' e realiza o clique."""
    parent_handle,_=get_main_window_handle_and_title()
    handle_pane = find_imprimir_button_in_pane(parent_handle)
    abre_janela_imprimir(handle_pane)
    defini_quantidade_de_impressao(parent_handle, copias)
    
    app = Application(backend='uia').connect(handle=parent_handle)
    parent_window = app.window(handle=parent_handle)
    time.sleep(2)
    # Localizar o botão "Imprimir"
    botao_imprimir = parent_window.child_window(auto_id="1", control_type="Button", class_name="Button")

    if botao_imprimir.exists():
        botao_imprimir.click()  # Clicar no botão
        
        print("Botão 'Imprimir' clicado.")
        return True
    else:
        print("Botão 'Imprimir' não encontrado.")
        return False
    

