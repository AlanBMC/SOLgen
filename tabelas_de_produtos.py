
from adiciona_produtos import * 
import flet as ft

def pagina_tabelas(page):
    page.title = "Tabelas"
    colunas = []
    data_novo = None
    def tipo_arquivo(e):
        nonlocal data_novo
        data_novo = extrai_dados_xml()
        atualizar_tabela()
        page.update()


    
    def atualizar_tabela():
        nonlocal colunas
        colunas.clear()  # Limpa as colunas anteriores
        if data_novo:
            for valores in data_novo:
                nome = ft.TextField(value=valores['nome'], color='#191810')
                codigo = ft.TextField(value=valores['codigo_de_barras'], color='#191810')
                preco_unitario = ft.TextField(value=float(valores['valor_unitario_comercial']), color='#191810')
                preco_revenda = ft.TextField(value=float(valores['valor_total']), color='#191810')
                colunas.append(ft.DataRow(cells=[
                    ft.DataCell(nome),
                    ft.DataCell(codigo),
                    ft.DataCell(preco_unitario),
                    ft.DataCell(preco_revenda)
                ]))
    tipo_de_arquivo = ft.ElevatedButton('XML', on_click=tipo_arquivo)

    tabela = ft.DataTable(
        width=700,
        bgcolor='#f0e162',
        data_row_color='#9c9c9c',
        columns=[ft.DataColumn(ft.Text('Nome do produto', color='#191810')), ft.DataColumn(ft.Text('Codigo de barras', color='#191810')), ft.DataColumn(ft.Text('preco unitario', color='#191810')), ft.DataColumn(ft.Text('Preco de revenda', color='#191810'))
        ],
        rows=colunas
    )
    page.update()
    coluna_com_scroll = ft.Column(
        controls=[tabela],
        scroll="always",  # Ativa o scroll vertical
        expand=True  # Expande a coluna para ocupar o espaço disponível
    )
    return coluna_com_scroll, tipo_de_arquivo

