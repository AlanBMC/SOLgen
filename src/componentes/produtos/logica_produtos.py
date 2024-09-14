from componentes.produtos.adiciona_produtos import *
import flet as ft
from math import ceil
from componentes.produtos.pyautogui_cadastra_produtos import manipula_dados
import asyncio
import re
class LogicaProdutos:
    def __init__(self, page,colunas):
        self.data_produtos = []
        self.colunas = colunas
        self.page = page
        self.porcetagem = 1
        self.mensagem_status = ft.Text(value="", color="blue")
    def tipo_arquivo(self,e):
        self.data_produtos = extrai_dados_xml()
        self.atualizar_tabela()

    def atualizar_tabela(self):
        self.colunas.clear()
        if self.data_produtos:
            for valores in self.data_produtos:
                nome = ft.TextField(value=valores['nome'], color='#191810', keyboard_type='nome')
                codigo = ft.TextField(value=valores['codigo_de_barras'], color='#191810', keyboard_type='codigo')
                cfop = ft.TextField(value=valores['cfop'], color='#191810', width=400, keyboard_type='cfop')
                ncm = ft.TextField(value=valores['ncm'], color='#191810', keyboard_type='ncm')
                preco_unitario = ft.TextField(value=float(valores['valor_unitario_comercial']), color='#191810', keyboard_type='precoUN')
                preco_revenda_valor = float(valores['valor_unitario_comercial'])
                if self.porcetagem:
                    preco_revenda_valor *= float(self.porcetagem)

                preco_revenda = ft.TextField(value=str(ceil(preco_revenda_valor)), color='#191810', keyboard_type='preco_revenda')

                self.colunas.append(ft.DataRow(cells=[
                    ft.DataCell(nome),
                    ft.DataCell(codigo),
                    ft.DataCell(preco_unitario),
                    ft.DataCell(preco_revenda),
                    ft.DataCell(ncm),
                     ft.DataCell(cfop)
                ]))

            self.page.update()
    def logica_porcentagem(self, e):
        self.porcetagem = re.sub(r'[^0-9.%]', '', e.control.value)
        e.control.value = self.porcetagem
        self.atualizar_tabela()
        self.page.update()


    
    def adiciona_produtos_vazio(self,e):
        """
        Adiciona uma linha de produto com campos vazios na tabela.
        """
        nome = ft.TextField(value="", color='#191810', bgcolor='#e4e4ac',keyboard_type='nome')
        codigo = ft.TextField(value="", color='#191810',bgcolor='#e4e4ac', keyboard_type='codigo')
        cfop = ft.TextField(value="", color='#191810',bgcolor='#e4e4ac',  keyboard_type='cfop')
        ncm = ft.TextField(value="", color='#191810',bgcolor='#e4e4ac', keyboard_type='ncm')
        preco_unitario = ft.TextField(value="", color='#191810', bgcolor='#e4e4ac',keyboard_type='precoUN')
        preco_revenda = ft.TextField(value="", color='#191810', bgcolor='#e4e4ac',keyboard_type='preco_revenda')

        # Adiciona a linha de produto com campos vazios à tabela
        self.colunas.append(ft.DataRow(cells=[
            ft.DataCell(nome),
            ft.DataCell(codigo),
            ft.DataCell(preco_unitario),
            ft.DataCell(preco_revenda),
            ft.DataCell(ncm),
            ft.DataCell(cfop)
        ]))
        self.page.update()



    def cadastra_produtos(self, e):
        lista_produtos_para_cadastro = []  # Inicializa a lista que armazenará os produtos

        # Loop pelas linhas da tabela
        for linha in self.colunas:
            nome = ""
            preco = ""
            codigo_de_barras = ""
            cfop = ""
            ncm = ""
            precoUN = ""

            # Loop pelas células da linha
            for celula in linha.cells:
                if isinstance(celula.content, ft.TextField):
                    if celula.content.keyboard_type == 'nome':
                        nome = celula.content.value
                    elif celula.content.keyboard_type == 'preco_revenda':
                        preco = celula.content.value
                    elif celula.content.keyboard_type == 'codigo':
                        codigo_de_barras = celula.content.value
                    elif celula.content.keyboard_type == 'cfop':
                        cfop = celula.content.value
                    elif celula.content.keyboard_type == 'ncm':
                        if celula.content.value:
                            ncm = celula.content.value
                    elif celula.content.keyboard_type == 'precoUN':
                        if celula.content.value:
                            precoUN = celula.content.value

            # Só adiciona o produto se tiver algum valor
            if nome or preco or codigo_de_barras or cfop or ncm or precoUN:
                dicio_lista = {
                    'nome': nome,
                    'codigo_de_barras': codigo_de_barras,
                    'cfop': cfop,
                    'ncm': ncm,
                    'preco': preco,
                    'precoUN': precoUN
                }
                lista_produtos_para_cadastro.append(dicio_lista)

        # Chama a função que manipula os dados
        manipula_dados(lista_produtos_para_cadastro)
    
    async  def atualiza_json(self, e):
        self.mensagem_status.value = "Atualizando dados, por favor aguarde..."
        self.page.add(self.mensagem_status)
        self.page.update()
        await asyncio.to_thread(atualiza_dados)
        self.mensagem_status.value = "Dados atualizados com sucesso."
        self.page.add(self.mensagem_status)

        self.page.update()
    