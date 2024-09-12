import win32con
import win32api
import win32gui
import time

def try_set_foreground(handle_da_janela):
    """
    Tenta trazer a janela para o primeiro plano.
    """
    try:
        # Verificar se a janela está visível e habilitada
        if win32gui.IsWindowVisible(handle_da_janela) and win32gui.IsWindowEnabled(handle_da_janela):
            win32gui.SetForegroundWindow(handle_da_janela)
        else:
            print("A janela não está visível ou habilitada.")
            # Como alternativa, minimizar e restaurar a janela
            win32gui.ShowWindow(handle_da_janela, win32con.SW_MINIMIZE)
            win32gui.ShowWindow(handle_da_janela, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(handle_da_janela)
    except Exception as e:
        print(f"Erro ao trazer a janela para o primeiro plano: {str(e)}")
        # Tentar simular a tecla ALT para forçar o foco
        win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)  # Pressionar ALT
        win32gui.SetForegroundWindow(handle_da_janela)   # Tentar novamente trazer a janela para o primeiro plano
        win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0)  # Soltar ALT

def limpa(handle_da_janela):
    """
    Limpa o conteúdo da janela com atalhos de teclado.
    """
    try_set_foreground(handle_da_janela)  # Tentar trazer a janela para o primeiro plano
    time.sleep(0.1)  # Pausa curta para garantir que a janela está ativa
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)  # Pressiona Ctrl
    win32api.keybd_event(0x41, 0, 0, 0)  # Pressiona "A" (Selecionar tudo)
    win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)  # Solta "A"
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)  # Solta Ctrl
    win32api.keybd_event(win32con.VK_BACK, 0, 0, 0)  # Pressiona Backspace (Apagar)
    win32api.keybd_event(win32con.VK_BACK, 0, win32con.KEYEVENTF_KEYUP, 0)  # Solta Backspace

def abre_janela_imprimir(handle):
    """
    Simula o comando para abrir a janela de impressão (Ctrl + P).
    """
    try_set_foreground(handle)  # Tentar trazer a janela para o primeiro plano
    time.sleep(0.1)  # Pausa curta para garantir que a janela está ativa
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)  # Pressiona Ctrl
    win32api.keybd_event(0x50, 0, 0, 0)  # Pressiona "P" (Imprimir)
    win32api.keybd_event(0x50, 0, win32con.KEYEVENTF_KEYUP, 0)  # Solta "P"
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)  # Solta Ctrl
