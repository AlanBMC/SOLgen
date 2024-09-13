import flet as ft
from componentes.produtos.logica_produtos import *



class ViewProdutos:
    def __init__(self, page):
        self.page = page
        self.colunas_produtos = []
        self.logica_produtos = LogicaProdutos()
        self.tabela = ft.DataTable(
                width=700,
                bgcolor='#f0e162',
                data_row_color='#9c9c9c',
                columns=[ft.DataColumn(ft.Text('Nome do produto', color='#191810')), ft.DataColumn(ft.Text('Codigo de barras', color='#191810')), ft.DataColumn(ft.Text('preco unitario', color='#191810')), ft.DataColumn(ft.Text('Preco de revenda', color='#191810'))
                ],
                rows=self.colunas_produtos
            )
        self.tipo_de_arquivo = ft.ElevatedButton('XML', on_click=self.logica_produtos.tipo_arquivo)
    def componentes(self):
        self.page.update()
        self.coluna_com_scroll = ft.Column(
        controls=[self.tabela],
        scroll="always",  # Ativa o scroll vertical
        expand=True  # Expande a coluna para ocupar o espaço disponível
    )
        return self.coluna_com_scroll, self.tipo_de_arquivo
