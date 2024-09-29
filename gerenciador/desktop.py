import os
import webview
import threading
import time
import subprocess

def run_django():
    # Executa o servidor Django sem bloquear a execução
    subprocess.Popen(['python', 'manage.py', 'runserver'], shell=True)

if __name__ == '__main__':
    # Inicia o servidor Django em uma thread separada
    django_thread = threading.Thread(target=run_django)
    django_thread.daemon = True
    django_thread.start()

    # Cria a janela do PyWebview apontando para o servidor Django
    webview.create_window('SOLgen', 'http://127.0.0.1:8000')
    webview.start()
