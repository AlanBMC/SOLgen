import pyperclip
import pyautogui
from pywinauto import Application
from time import sleep
def cadastraprod(produtos):
    #abre
    #entra no cadastro
    #sleep(2)
    #pyautogui.click(x = 256, y = 606) #clica proprietário
    #sleep(2)
    #pyautogui.click(x = 79, y = 584)  #clica em cadastro
    #sleep(2)
    #pyautogui.click(x = 662, y = 218) #clica no segundo botão o cadastro
    #sleep(2)
    for produto in produtos:
        # Novo item
        sleep(2)
        pyautogui.click(x=1239, y=185)
        sleep(1)
        # Clica em OK
        click_ok()

        # Nome do item
        pyautogui.click(x=715, y=280)
        enter_text(produto['nome'])
        sleep(0.5)

        # Clica na janela de fiscal
        pyautogui.click(x=612, y=307)
        sleep(1)

        # Clica no input de NCM
        pyautogui.click(x=729, y=353)
        digita_texto(produto['ncm'])
        sleep(1)
        

        
        # Volta para geral
        pyautogui.click(x=416, y=306)
        sleep(1)

        # Coloca o código
        pyautogui.click(x=590, y=334)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        enter_text(produto['codigo_de_barras'])
        sleep(1)

        # Coloca preço de revenda
        pyautogui.click(x=577, y=592)
        enter_text(produto['valor_revenda'])
        sleep(1)

        # Salva item
        pyautogui.click(x=1460, y=187)
        sleep(1)

        # Aperta ok após salvar
        click_ok()
        sleep(2)  # Esperar o item ser salvo




def apaga_texto():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

def enter_text(text):
    pyperclip.copy(text)
    sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)

def click_ok():
    sleep(1)
    pyautogui.click(x=1154, y=562)

def digita_texto(texto):
    pyautogui.write(texto, interval=0.1)

def abrepdv():
    try:
        # Tenta conectar-se ao BarTender já aberto
        app = None
        caminho_arquivo = ''
        try:
            # Tenta conectar-se ao BarTender em execução
            app = Application(backend="uia").connect(path='caminho do arquivo')
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
            app = Application(backend="uia").start(f'"{caminho_arquivo}"')
            sleep(15)  # Esperar o BarTender carregar completamente

        # Obter a janela principal do BarTender
        window = app.top_window()

        # Traz a janela para o foco e maximiza (caso ainda não tenha sido feita)
        window.set_focus()
        window.maximize()
        print(f"BarTender iniciado com o arquivo {caminho_arquivo}.")
        
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
            sleep(15)  # Esperar o BarTender carregar completamente

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
    

def automacao_pyautogui_impressora(request, produtos):
    for produto in produtos:
        print(produto.nome, produto.preco, produto.codigo_de_barras)
        #etiqueta amarela
        sleep(1)
        pyautogui.click(x = 665, y = 294)
        sleep(2)
        pyautogui.click(x = 665, y = 294) # posicao do nome
        apaga_texto()
        #escreve
        enter_text(produto.nome)
        sleep(1)
        pyautogui.click(x = 642, y = 409)#preço
        apaga_texto()
        #escreve
        enter_text(f'R$ - {produto.preco:.2f}')
        pyautogui.doubleClick(x = 702, y = 554)#codigo de barras
        sleep(2)
        pyautogui.click(x = 794, y = 286) # segunda tela do codigo de barras
        apaga_texto()
        #escreve
        enter_text(produto.codigo_de_barras)
        sleep(1)
        pyautogui.click(x = 925, y = 687)#botao fechar da segunda janela do codigo de barras
        sleep(2)
        pyautogui.click(x = 1109, y = 226) #espaço fora dos campos texto para ter um press
        pyautogui.hotkey('ctrl', 'p')
        sleep(4)
        pyautogui.click(x = 681, y = 375) # quantidade
        apaga_texto()
        enter_text('1') #coloca quantidade
        
        pyautogui.click(x = 596, y = 583) # botao imprime
    
    return True