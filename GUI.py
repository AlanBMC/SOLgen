import flet as ft
from busca_produtos import *
from impressao import *

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


ft.app(main)
