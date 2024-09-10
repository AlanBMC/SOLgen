import json

# Arquivos de entrada e saída
arquivo_txt = 'codigos.txt'
arquivo_json = 'dados_extracao.json'
arquivo_saida_json = 'produtos_para_impressao.json'

# Função para ler o arquivo TXT e retornar os códigos
def ler_codigos_txt(arquivo_txt):
    with open(arquivo_txt, 'r') as file:
        codigos = file.read().splitlines()  # Lê as linhas e remove quebras de linha
    return codigos

# Função para ler o arquivo JSON e retornar os dados
def ler_dados_json(arquivo_json):
    with open(arquivo_json, 'r', encoding='utf-8') as file:
        dados = json.load(file)
    return dados

# Função para comparar os códigos e gerar um novo JSON
def comparar_codigos(codigos_txt, dados_json):
    produtos_para_impressao = []
    
    for produto in dados_json:
        if produto['codigo'] in codigos_txt:
            print(codigos_txt)
            produtos_para_impressao.append(produto)
    
    # Salva o novo arquivo JSON com os produtos para impressão
    with open(arquivo_saida_json, 'w', encoding='utf-8') as file:
        json.dump(produtos_para_impressao, file, ensure_ascii=False, indent=4)

    print(f"Novo arquivo JSON salvo como '{arquivo_saida_json}'")

# Executa o fluxo de trabalho
if __name__ == "__main__":
    # Lê os códigos do arquivo TXT
    codigos_txt = ler_codigos_txt(arquivo_txt)
    # Lê os dados do arquivo JSON
    dados_json = ler_dados_json(arquivo_json)
    
    # Compara os códigos e cria um novo JSON com os produtos encontrados
    comparar_codigos(codigos_txt, dados_json)
