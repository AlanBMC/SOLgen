from pywinauto import Application
import pywinauto
import win32gui
def get_main_window_handle_and_title():
    """Retorna o handle e o nome (título) da janela principal."""
    handle = win32gui.FindWindow("BartendWindowClass", None)
    if handle:
        # Obter o nome da janela
        window_title = win32gui.GetWindowText(handle)
        return handle, window_title
    else:
        return None, None
    
def find_subwindow_by_name_and_class(parent_handle, subwindow_name, subwindow_class):
    """Procura uma subjanela com base no nome e na classe."""
    app = Application(backend='uia').connect(handle=parent_handle)

    # Obter a janela pai a partir do handle
    parent_window = app.window(handle=parent_handle)

    # Localizar a subjanela pelo nome e classe
    subwindow = parent_window.child_window(title=subwindow_name, control_type="Window", class_name=subwindow_class)

    if subwindow.exists():
        print(f"Subjanela '{subwindow_name}' encontrada.")
        return subwindow.handle
    else:
        print(f"Subjanela '{subwindow_name}' não encontrada.")
        return None

def find_field_by_automation_id(parent_handle, automation_id, class_name=None):
    """Procura por um controle dentro de uma janela pai usando AutomationId e ClassName."""
    # Conectar à aplicação já aberta através do handle
    app = Application(backend='uia').connect(handle=parent_handle)

    # Obter a janela pelo handle
    parent_window = app.window(handle=parent_handle)

    # Localizar o campo usando o AutomationId
    field = parent_window.child_window(auto_id=automation_id, control_type="Document", class_name=class_name)

    if field.exists():
        return field.handle
    else:
        return None


def handle_campo_codigo():
    # Handle da janela pai
    handle, parent_handle = get_main_window_handle_and_title()  # Substitua com o handle correto

    # Buscar o campo com AutomationId e ClassName especificados
    field_handle = find_field_by_automation_id(handle, "11054", "RICHEDIT50W")

    if field_handle:
        print(f"Handle do campo encontrado: {field_handle}")
        return field_handle
    else:
        print("Campo não encontrado.")


def clicar_botao_ok(main_handle):
    """Função para clicar no botão OK."""
    subwindow_handle = find_subwindow_by_name_and_class(main_handle, "Editar dados", "#32770")
    app = Application(backend='uia').connect(handle=subwindow_handle)

    # Obter a janela a partir do handle
    parent_window = app.window(handle=subwindow_handle)

    # Buscar o botão "OK" pelo AutomationId e ClassName
    botao_ok = parent_window.child_window(auto_id="1", control_type="Button", class_name="Button")

    if botao_ok.exists():
        # Clicar no botão
        botao_ok.click()
        print("Botão OK clicado.")
    else:
        print("Botão OK não encontrado.")
#NativeWindowHandle	3476766


