import flet as ft
from componentes.impressora.logica_impressora import ImpressoraLogica

class ImpressoraView:
    def __init__(self, page):
        self.page = page
        self.cards_list = ft.GridView(
            expand=True,
            max_extent=200,  # Width of each card
            spacing=10,
            run_spacing=10,
            child_aspect_ratio=1
        )
        self.logicaImpressora = ImpressoraLogica(self.adiciona_card, self.atualizar_cards)

    def componenetes(self):
        """
        metodos de componenetes dsa pagina impressora
        """


        self.input_codigo = ft.TextField(
        label="Escaneie o código do produto",
        bgcolor='#525252', color="#fafa3c", on_submit=self.logicaImpressora.pesquisa_codigo, autofocus=True
    )
        self.input_quantidade_por_produto = ft.Dropdown(
        width=100, options=[ft.dropdown.Option(1), ft.dropdown.Option(2), ft.dropdown.Option(3), ft.dropdown.Option(4)]
    )
        self.tipo_etiqueta = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value=1, label="Etiqueta Amarela"),
            ft.Radio(value=2, label="Etiqueta Branca")
        ])
    )   
        self.enviar_impressao = ft.ElevatedButton(
        'Enviar impressão', on_click=lambda e: self.logicaImpressora.prepara_dados_para_impressao(self.tipo_etiqueta.value))
        
        return ft.Column(
            controls=[
            self.input_codigo,
            self.tipo_etiqueta,
            self.enviar_impressao,
            ]
        )
