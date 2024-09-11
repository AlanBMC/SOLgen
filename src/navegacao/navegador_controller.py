from flet import *
from navegacao.logica_navegacao import paginaEscolhida

class Navegador:
    def __init__(self,page:Page):
        self.page = page
        self.navbar = NavigationBar(
            destinations=[
                NavigationBarDestination(icon=icons.HOME, label="Home"),
                NavigationBarDestination(icon=icons.PRINT, label="Impressora"),
            ],
            on_change=paginaEscolhida
        )
    def nav(self):
        return self.navbar