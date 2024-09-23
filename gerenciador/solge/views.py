from django.shortcuts import render # type: ignore
import pdfplumber
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
    return render(request, 'tabela.html')


def extrai_dados(arquivo_pdf):
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
                    preco = tabela_filtrada[2][0]
                                    
                    item = {
                        "nome": nome,
                        "codigo": codigo,
                        "preco": preco
                    }
                    dados.append(item)
                elif len(tabela_filtrada) >3:
                    nome = tabela_filtrada[0][0][5:] + tabela_filtrada[1][0]
                    codigo =  tabela_filtrada[2][0] # Exemplo de uso
                    preco = tabela_filtrada[3][0]
                    item = {
                        "nome": nome,
                        "codigo": codigo,
                        "preco": preco
                    }
                    dados.append(item)