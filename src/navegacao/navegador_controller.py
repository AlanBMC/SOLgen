from flet import *
from componentes.impressora.view_impressora import ImpressoraView
from componentes.produtos.view_produtos import ProdutosView
class Navegador:
    def __init__(self,page:Page):
        self.page = page
        self.navbar = NavigationBar(
            destinations=[
                NavigationBarDestination(icon=icons.HOME, label="Home"),
                NavigationBarDestination(icon=icons.PRINT, label="Impressora"),
                NavigationBarDestination(icon=icons.ADD_SHOPPING_CART_ROUNDED, label='Produtos')
            ],
            on_change=self.paginaEscolhida
        )
    def nav(self):
        return self.navbar
    
    def paginaEscolhida(self, e):
        self.page.controls.clear()
        if e.control.selected_index == 0:
            pass
        elif e.control.selected_index == 1:
            print( e.control.selected_index )
            page_impressora = ImpressoraView(self.page)
            self.page.add(page_impressora.componentes())
        elif e.control.selected_index == 2:
            page_produtos = ProdutosView(self.page)
            self.page.add(page_produtos.componentes())