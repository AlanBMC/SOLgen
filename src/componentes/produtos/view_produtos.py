import flet as ft
from componentes.produtos.logica_produtos import *

#Criar logica para pegar os dados da tabela e manipular - multiplicar por 2, adicioanar valor opcional e mandar para o pyautogui
class ProdutosView:
    def __init__(self, page):
        self.page = page
        self.colunas_produtos = []
        self.logica_produtos = LogicaProdutos(self.page,self.colunas_produtos)
        self.tabela = ft.DataTable(
            width=800,
            bgcolor='#f0e162',
            heading_row_height=100,
            data_row_color='#d6d66e',
            columns=[ft.DataColumn(ft.Text('Nome do produto', color='#191810')),
                      ft.DataColumn(ft.Text('Codigo de barras', color='#191810')),
                        ft.DataColumn(ft.Text('preco unitario', color='#191810')),
                          ft.DataColumn(ft.Text('Preco de revenda', color='#191810')),
                          ft.DataColumn(ft.Text('NCM', color='#191810')),
                          ft.DataColumn(ft.Text('CFOP', color='#191810')),
                     ],
            rows=self.colunas_produtos
        )

        
    def componentes(self):
        self.tabela_gui()
        self.botoes_gui()
        return self.layoutGeral()
    

    def tabela_gui(self):
        self.coluna_com_scroll =ft.Container(

        ft.Column(
            controls=[self.tabela],
            scroll="auto",  # Ativa o scroll vertical
            expand=True  # Expande a coluna para ocupar o espaço disponível
        ),
         height=400
        ) 


    def botoes_gui(self):
        valor_porcentagem = ft.TextField(label='Porcentagem', on_submit=self.logica_produtos.logica_porcentagem)
        cadastrar_produtos = ft.ElevatedButton('Cadastrar produtos', on_click=self.logica_produtos.cadastra_produtos)
        self.tipo_de_arquivo = ft.ElevatedButton(
            'XML', on_click=self.logica_produtos.tipo_arquivo)
        self.botoes_colunas = ft.Column(
            controls=[
                self.tipo_de_arquivo,
                valor_porcentagem,
                cadastrar_produtos
                
            ],
            alignment=ft.MainAxisAlignment.START
        )
    
    def layoutGeral(self):
        self.layout_geral = ft.Row(
        controls=[
            self.botoes_colunas,       # Botões à direita
            self.coluna_com_scroll  # Tabela à esquerda
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,  # Alinha os itens ao topo da linha
        expand=True
    )
        return self.layout_geral