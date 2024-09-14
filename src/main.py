import flet as ft
from componentes.navegacao.navegador_controller import Navegador

def main(page:ft.Page):
    page.Title = 'Sistema de Gerenciamento SOLgen'
    menu = Navegador(page)
    page.add(menu.nav())

ft.app(main)