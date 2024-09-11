import flet as ft
from busca_produtos import *
from impressao import *
from adiciona_produtos import *
itens_lidos = []
cards_list = ft.GridView(
    expand=True,
    max_extent=200,  # Width of each card
    spacing=10,
    run_spacing=10,
    child_aspect_ratio=1
)


def main(page: ft.Page):
    def impressoras(e):
        for remove_home in lista_homePage:
            page.remove(remove_home)
        for i in lista_impressora:
            page.add(i)
        page.update()

    def homepage(e):
        for i in lista_impressora:
            page.remove(i)
        for homes in lista_homePage:
            page.add(homes)
        page.update()

    def excluir_produto(e):
        produto = e.control.data
        if produto in itens_lidos:
            itens_lidos.remove(produto)
            atualizar_cards()

    def adicionar_card(produto):
        card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(produto['nome'], max_lines=1, overflow="ellipsis",
                                bgcolor='#FFFFFF', color='#158711'),
                        ft.Text(produto['preco']),
                        ft.Text(produto['codigo']),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Excluir", on_click=excluir_produto, data=produto)
                            ],
                            alignment=ft.MainAxisAlignment.END
                        )
                    ]
                ),
                width=200, padding=10, bgcolor="#E9D345", border_radius=8
            ),
        )
        cards_list.controls.append(card)

    def atualizar_cards():
        cards_list.controls.clear()
        for produto in itens_lidos:
            adicionar_card(produto)
        cards_list.update()

    def pesquisa_codigo(e):
        codigo = e.control.value.strip()

        produto = encontrar_produto_por_codigo(codigo)

        if produto and produto not in itens_lidos:
            itens_lidos.append(produto)
            adicionar_card(produto)
            input_codigo.value = ''
            input_codigo.focus()
        page.update()
        input_codigo.autofocus = True

    input_codigo = ft.TextField(
        label="Escaneie o código do produto",
        bgcolor='#525252', color="#fafa3c", on_submit=pesquisa_codigo, autofocus=True
    )
    
    
    def prepara_dados_para_impressao(e):
        quantidade = input_quantidade_por_produto.value
        eti = tipo_etiqueta.value
        if eti is None:
            print("Tipo de etiqueta não selecionado.")
            page.add(ft.Text('Por favor, selecione um tipo de etiqueta.'))
            page.update()
            return
        if envia_para_impressora(itens_lidos, int(eti), quantidade):
            page.add(ft.Text('Impressão acontecendo...'))
            page.update()

    input_quantidade_por_produto = ft.Dropdown(
        width=100, options=[ft.dropdown.Option(1), ft.dropdown.Option(2), ft.dropdown.Option(3), ft.dropdown.Option(4)]
    )

    tipo_etiqueta = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value=1, label="Etiqueta Amarela"),
            ft.Radio(value=2, label="Etiqueta Branca")
        ])
    )

    enviar_impressao = ft.ElevatedButton(
        'Enviar impressão', on_click=prepara_dados_para_impressao)
    tabela, botao_tipo_de_visualizacao = pagina_tabelas(page)
    homePage = ft.ElevatedButton("HomePage", on_click=homepage)
    lista_homePage = [ft.Row([ft.ElevatedButton(
        "Impressora", on_click=impressoras), homePage, tabela, botao_tipo_de_visualizacao ])]
    lista_impressora =[homePage,input_codigo, tipo_etiqueta,
                        input_quantidade_por_produto, enviar_impressao, cards_list]
    page.add(*lista_homePage)



def pagina_tabelas(page:ft.Page):
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
                preco_revenda = ft.TextField(value=float(valores['valor_revenda']), color='#191810')
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
ft.app(main)
