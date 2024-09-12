from componentes.impressora.busca_produtos import *
import flet as ft 
class ImpressoraLogica:
    def __init__(self, card_list):
        self.produtos_lidos = []
        self.card_list = card_list



    def pesquisa_codigo(self,e):
        codigo = e.control.value.strip()
        produto = encontrar_produto_por_codigo(codigo)
        if produto and produto not in self.produtos_lidos:
            self.produtos_lidos.append(produto)
            self.callback_adiciona_card(produto)
            #adcionar card
        
    def prepara_dados_para_impressao(e,quantidade, tipo_etiqueta):
        pass
       
    def excluir_produto(self,e):
        produto = e.control.data
        if produto in self.produtos_lidos:
            self.produtos_lidos.remove(produto)
            self.callback_atualizar_cards()

    def adiciona_card(self,produto):
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
                                    "Excluir", on_click=lambda e: self.logicaImpressora.excluir_produto(e,self.cards_list), data=produto)
                            ],
                            alignment=ft.MainAxisAlignment.END
                        )
                    ]
                ),
                width=200, padding=10, bgcolor="#E9D345", border_radius=8
            ),
        )
            self.cards_list.controls.append(card)
            self.cards_list.update()
    def atualizar_cards(self ):
        self.cards_list.controls.clear()
        for produto in self.produtos_lidos:
            self.callback_adiciona_card(produto)
        self.card_list.update()