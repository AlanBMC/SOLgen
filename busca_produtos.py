import json
try:
    with open('dados_extraidos.json', encoding='utf-8') as data_json:
        data = json.load(data_json)

except FileNotFoundError:
    data = []
    print("Arquivo 'dados_extracao.json' não encontrado. Verifique o caminho e tente novamente.")

def encontrar_produto_por_codigo(codigo):
    for item in data:
        if item["codigo"] == codigo:
            return item
    return None