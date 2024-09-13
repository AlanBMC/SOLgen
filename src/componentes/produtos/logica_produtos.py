from componentes.produtos.adiciona_produtos import *
import flet as ft
from math import ceil, floor

import re
class LogicaProdutos:
    def __init__(self, page,colunas):
        self.data_produtos = []
        self.colunas = colunas
        self.page = page
        self.porcetagem = 1

    def tipo_arquivo(self,e):
        self.data_produtos = extrai_dados_xml()
        self.atualizar_tabela()

    def atualizar_tabela(self):
        self.colunas.clear()
        if self.data_produtos:
            for valores in self.data_produtos:
                nome = ft.TextField(value=valores['nome'], color='#191810', keyboard_type='nome')
                codigo = ft.TextField(value=valores['codigo_de_barras'], color='#191810', keyboard_type='codigo')
                cfop = ft.TextField(value=valores['cfop'], color='#191810', width=400, keyboard_type='cfop')
                ncm = ft.TextField(value=valores['ncm'], color='#191810', keyboard_type='ncm')
                preco_unitario = ft.TextField(value=float(valores['valor_unitario_comercial']), color='#191810', keyboard_type='preco_un')
                preco_revenda_valor = float(valores['valor_unitario_comercial'])
                if self.porcetagem:
                    preco_revenda_valor *= float(self.porcetagem)

                preco_revenda = ft.TextField(value=str(ceil(preco_revenda_valor)), color='#191810', keyboard_type='preco_revenda')

                self.colunas.append(ft.DataRow(cells=[
                    ft.DataCell(nome),
                    ft.DataCell(codigo),
                    ft.DataCell(preco_unitario),
                    ft.DataCell(preco_revenda),
                    ft.DataCell(ncm),
                     ft.DataCell(cfop)
                ]))
            self.page.update()
    def logica_porcentagem(self, e):
        self.porcetagem = re.sub(r'[^0-9.%]', '', e.control.value)
        e.control.value = self.porcetagem
        self.atualizar_tabela()
        self.page.update()

    def cadastra_produtos(self, e):
        lista_produtos_para_cadatrastro = []
        nome = ""
        preco = ""
        codigo_de_barras = ""
        cfop = ""
        ncm = ""
    
        for linha in self.colunas:
            for celula in linha.cells:
                if isinstance(celula.content, ft.TextField):
                    if celula.content.keyboard_type == 'nome':
                        nome =celula.content.value
                    elif celula.content.keyboard_type == 'preco_revenda':
                        preco =celula.content.value
                    elif celula.content.keyboard_type == 'codigo':
                        codigo_de_barras= celula.content.value
                    elif celula.content.keyboard_type == 'cfop':
                        cfop = celula.content.value
                    elif celula.content.keyboard_type == 'ncm':
                        ncm = celula.content.value
                    dicio_lista = {
                        'nome':nome,
                        'codigo_de_barras':codigo_de_barras,
                        'cfop':cfop,
                        'ncm':ncm,
                        'preco':preco
                    }
                    lista_produtos_para_cadatrastro.append(dicio_lista)
        print(lista_produtos_para_cadatrastro)