from componentes.impressora.busca_produtos import *
import flet as ft 
from componentes.impressora.impressao import envia_para_impressora
class ImpressoraLogica:
    def __init__(self, card_list):
        self.produtos_lidos = []
        self.card_list = card_list

    def pesquisa_codigo(self,e):
        codigo = e.control.value.strip()
        e.control.value = ""
        e.control.focus() 
        produto = encontrar_produto_por_codigo(codigo)
        if produto and produto not in self.produtos_lidos:
            self.produtos_lidos.append(produto)
            self.adiciona_card(produto)
            #adcionar card 
        e.page.update()
    def prepara_dados_para_impressao(self,e, tipo_etiqueta):
        dados = []
        for card in self.card_list.controls:
            coluna = card.content.content  # Acessa a `Column` dentro do `Container`
            nome = coluna.controls[0].value  # Primeiro Text (nome)
            preco = coluna.controls[1].value  # Segundo Text (preço)
            codigo = coluna.controls[2].value  # Terceiro Text (código)
            produto = {
                "nome": nome,
                "preco": preco,
                "codigo": codigo
            }
            dados.append(produto)
        envia_para_impressora(dados, 1,  tipo_etiqueta.value)
    def excluir_produto(self,e):
        produto = e.control.data
        if produto in self.produtos_lidos:
            self.produtos_lidos.remove(produto)
            self.atualizar_cards()

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
                                    "Excluir", on_click=self.excluir_produto, data=produto)
                            ],
                            alignment=ft.MainAxisAlignment.END
                        )
                    ]
                ),
                width=200, padding=10, bgcolor="#E9D345", border_radius=8
            ),
        )
            self.card_list.controls.append(card)
            self.card_list.update()

    def atualizar_cards(self ):
        self.card_list.controls.clear()
        for produto in self.produtos_lidos:
            self.adiciona_card(produto)
        self.card_list.update()