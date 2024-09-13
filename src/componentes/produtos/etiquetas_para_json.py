import pdfplumber
import json
import re

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
# Exemplo de uso

                           
    with open('./SOLgen/src/json/dados_extraidos.json', 'w', encoding='utf-8') as json_file:
        json.dump(dados, json_file, ensure_ascii=False, indent=4)

    # Exibe os dados salvos para confirmação
    print(json.dumps(dados, ensure_ascii=False, indent=4))

# Exemplo de uso
