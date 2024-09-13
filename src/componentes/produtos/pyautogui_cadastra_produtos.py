import pyautogui
import pyperclip
import time

def digita_texto(texto):
    """
    Função para digitar texto caractere por caractere.
    
    :param texto: String a ser digitada.
    :return: Nenhum retorno.
    
    Esta função usa o pyautogui.write() para simular a digitação de texto em um campo
    onde o cursor está ativo. Há um intervalo entre as teclas para simular uma digitação mais humana.
    
    Exemplo de uso:
        digita_texto("Texto a ser digitado.")
    """
    time.sleep(0.5)  # Espera para garantir que o campo de texto esteja pronto
    pyautogui.write(texto, interval=0.05)  # Digita o texto, com intervalo de 0.05 segundos entre cada tecla


def cola_texto(texto):
    """
    Função para colar texto usando pyperclip e pyautogui.
    
    :param texto: String a ser colada.
    :return: Nenhum retorno.
    
    Esta função copia o texto para a área de transferência e em seguida
    usa o atalho de teclado Ctrl + V para colar o conteúdo no campo ativo.
    
    Exemplo de uso:
        cola_texto("Texto a ser colado.")
    """
    pyperclip.copy(texto)  # Copia o texto para a área de transferência
    time.sleep(0.5)  # Pausa para garantir que o texto foi copiado
    pyautogui.hotkey('ctrl', 'v')  # Cola o texto com Ctrl + V


def clica_ok():
    """
    Função reservada para simular o clique no botão 'OK'.
    
    :return: Nenhum retorno.
    
    Esta função está reservada para o futuro. Deve conter a lógica para localizar
    e clicar em um botão "OK" na interface da aplicação, provavelmente usando coordenadas de tela.
    
    Exemplo de uso:
        clica_ok()
    """
    pass


def clica_fiscal():
    """
    Função reservada para simular o clique na aba ou campo 'Fiscal'.
    
    :return: Nenhum retorno.
    
    Esta função está reservada para o futuro. Deve conter a lógica para localizar
    e clicar em uma aba ou campo relacionado a "Fiscal" na interface da aplicação.
    
    Exemplo de uso:
        clica_fiscal()
    """
    pass


def clica_cfop(cfop):
    """
    Função para digitar o valor do CFOP em um campo específico.
    
    :param cfop: String que representa o CFOP a ser digitado.
    :return: Nenhum retorno.
    
    Esta função utiliza a função digita_texto() para inserir o valor do CFOP em um campo.
    
    Exemplo de uso:
        clica_cfop("5102")
    """
    time.sleep(1)
    digita_texto(cfop)
    time.sleep(1)
    digita_texto(cfop)
    time.sleep(1)
    digita_texto(cfop)
    time.sleep(1)

def clica_ncm(ncm):
    """
    Função para digitar o valor do NCM em um campo específico.
    
    :param ncm: String que representa o NCM a ser digitado.
    :return: Nenhum retorno.
    
    Esta função utiliza a função digita_texto() para inserir o valor do NCM em um campo.
    
    Exemplo de uso:
        clica_ncm("12345678")
    """
    digita_texto(ncm)


def clica_nome(nome):
    """
    Função para colar o nome em um campo específico.
    
    :param nome: String que representa o nome a ser colado.
    :return: Nenhum retorno.
    
    Esta função utiliza a função cola_texto() para colar o nome no campo apropriado.
    
    Exemplo de uso:
        clica_nome("Nome do produto")
    """
    cola_texto(nome)


def clica_preco_revenda(preco):
    """
    Função para colar o valor do preço de venda em um campo específico.
    
    :param preco: String que representa o preço a ser colado.
    :return: Nenhum retorno.
    
    Esta função utiliza a função cola_texto() para colar o preço no campo apropriado.
    
    Exemplo de uso:
        clica_preco("199.99")
    """
    cola_texto(preco)


def clica_preco_compra(preco_un):
    """
    Função para colar o preço de compra (preço unitário) em um campo específico.
    
    :param preco_un: String que representa o preço de compra a ser colado.
    :return: Nenhum retorno.
    
    Esta função utiliza a função cola_texto() para colar o preço de compra no campo apropriado.
    
    Exemplo de uso:
        clica_preco_compra("149.99")
    """
    cola_texto(preco_un)


def clica_codigo_de_barras(codigo):
    """
    Funcao reservado para simular o clique no input codigo
    :return: Sem retorno
    :Param: recebe o codigo de barras do produto
    Exemplo de uso:
        clica_codigo_de_barras('12345678910')
    """


def clica_salvar():
    """
    Função reservada para simular o clique no botão 'Salvar'.
    
    :return: Nenhum retorno.
    
    Esta função está reservada para o futuro. Deve conter a lógica para localizar
    e clicar em um botão "Salvar" na interface da aplicação, provavelmente usando coordenadas de tela.
    
    Exemplo de uso:
        clica_salvar()
    """
    pass


def clica_novo_produto():
    """
    clica no botao novo
    :return: Nenhum retorno.

    """


def manipula_dados(produtos):
    """
    Função para manipular os dados dos produtos.
    recebe um dicionario com: nome, preco, codigo, ncm, cfop e precoUN
    chama as funçoes para controlar o mouse e teclado
    """
    nao = False
    print(produtos)
    if nao:
        for dados in produtos:
            time.sleep(1)
            clica_novo_produto()
            time.sleep(1)
            clica_ok()
            time.sleep(1)
            clica_nome(dados['nome'])
            time.sleep(1)
            clica_codigo_de_barras(dados['codigo'])
            time.sleep(1)
            clica_preco_revenda(dados['preco'])
            time.sleep(1)
            clica_preco_compra(dados['precoUN'])
            time.sleep(1)
            clica_fiscal()
            time.sleep(1)
            clica_ncm(dados['ncm'])
            time.sleep(1)
            clica_cfop(dados['cfop'])
            time.sleep(1)
            clica_salvar()
            time.sleep(1)