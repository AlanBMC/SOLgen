from componentes.produtos.adiciona_produtos import *
import flet as ft
import re
class LogicaProdutos:
    def __init__(self, page,colunas):
        self.data_produtos = []
        self.colunas = colunas
        self.page = page
        self.porcetagem = 1
    def tipo_arquivo(self,e):
        self.data_produtos = extrai_dados_xml()
        self.atualizar_tabela()

    def atualizar_tabela(self):
        self.colunas.clear()
        if self.data_produtos:
            for valores in self.data_produtos:
                nome = ft.TextField(value=valores['nome'], color='#191810')
                codigo = ft.TextField(value=valores['codigo_de_barras'], color='#191810')
                preco_unitario = ft.TextField(value=float(valores['valor_unitario_comercial']), color='#191810')
                preco_revenda_valor = float(valores['valor_unitario_comercial'])
                if self.porcetagem:
                    preco_revenda_valor*= float(self.porcetagem)
                
                preco_revenda = ft.TextField(value=str(preco_revenda_valor), color='#191810')

                self.colunas.append(ft.DataRow(cells=[
                    ft.DataCell(nome),
                    ft.DataCell(codigo),
                    ft.DataCell(preco_unitario),
                    ft.DataCell(preco_revenda)
                ]))
            self.page.update()
    def logica_porcentagem(self, e):
        self.porcetagem = re.sub(r'[^0-9.%]', '', e.control.value)
        e.control.value = self.porcetagem
        self.atualizar_tabela()
        self.page.update()