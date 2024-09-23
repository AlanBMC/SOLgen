from django.shortcuts import render # type: ignore

# Create your views here.
def home(request):
    return render(request, 'home.html')




def atualiza_data_base():
    """
    pega o arquivo PDF de etiquetas
    esxtrai os dados e salva no banco

    """
    

def impressora():
    """
    Compara os codigos recebidos com os do banco de dados
    prepara os codigos achados
    imprime os codigos achados

    """

def cadastro_produto(request):
    """
    pega xml, pdf
    extrai dados
    salva no banco e manda para funcao do pyautogui

    """

