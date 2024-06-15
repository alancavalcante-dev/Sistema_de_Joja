from tabulate import tabulate
import pandas as pd
from Loja import Loja

class Carrinho:
    
    def __init__(self, loja):
        self.loja = loja
        self.lista_de_produtos = []


    def adicionar_item(self, produto, qtd_itens):
        existe = False
        for prod_loja in self.loja.prod_loja:
            if produto.produto == prod_loja.produto:
                existe = True
        if not existe: raise Exception("Esse produto não existe na loja")
            
        if qtd_itens <= produto.qtd_estoque:
            produto.qtd_estoque -= qtd_itens
            item = {'produto': produto, 'qtd_itens': qtd_itens}
        else:
            item = {'produto': produto, 'qtd_itens': produto.qtd_estoque}
            print(f'Não temos a quantidade de itens que você escolheu, temos apenas: {produto.qtd_estoque} {produto.produto}. Você pegou todos')
            produto.qtd_estoque = 0

        prod_repetido = False
        for prod in self.lista_de_produtos:
            if prod['produto'].produto == produto.produto:
                prod['qtd_itens'] = prod['qtd_itens'] + qtd_itens
                prod_repetido = True
                break
        
        if not prod_repetido:
            self.lista_de_produtos.append(item)

        if len(self.lista_de_produtos) == 0:
            self.lista_de_produtos.append(item)
        

    def devolver_item(self, item, qtd_itens):
        existe = False
        for carrinho in self.lista_de_produtos:
            if item.produto == carrinho.produto:
                existe = True
        if not existe:
            raise Exception("Esse produto não existe no Carrinho")
        # diminuir do carrinho, e aumentar na loja
        


    def listar_carrinho(self):
        df_table = pd.DataFrame([{'produto': item['produto'].produto, 'preco': item['produto'].preco, 'qtd_produto': item['qtd_itens']} for item in self.lista_de_produtos])
        tabela_formatada = tabulate(df_table, headers=['Id','Produto','Preço','Qtd produto'], tablefmt="pipe")
        return tabela_formatada