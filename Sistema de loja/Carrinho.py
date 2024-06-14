from tabulate import tabulate
import pandas as pd
from Loja import Loja

class Carrinho:
    
    def __init__(self, loja):
        self.lista_de_produtos = []
        self.loja = loja

    def adicionar_item(self, produto, qtd_itens):   
        produto_existente = self.teste(produto.produto)

        if produto_existente == None:
            raise Exception("Não existe na loja!")
        
        item = {'produto': produto, 'qtd_itens': qtd_itens}

        # mesmo produto
        for i in self.lista_de_produtos: # percorrendo a lista dos itens (dict)
            #dict > obj > propri        # obj prod
            if i['produto'].produto == produto.produto:
                i['qtd_itens'] = i['qtd_itens'] + qtd_itens
                break

        # produto diferente


        # lista vazio
        if len(self.lista_de_produtos) == 0:
            self.lista_de_produtos.append(item)
        

    def remover_item(self, nome_produto):
        for produto in self.lista_de_produtos:
            if produto.produto == nome_produto:
                self.lista_de_produtos.remove(produto)
                print(f'Produto "{nome_produto}" removido da loja.')
                return
        print(f'Produto "{nome_produto}" não encontrado na loja.')

    def listar_carrinho(self):
        # Convertendo a lista de produtos para um DataFrame
        self.df_itens = pd.DataFrame([vars(produto) for produto in self.lista_de_produtos])
        
        # Usando tabulate para formatar a tabela
        tabela_listar = tabulate(self.df_itens, headers='keys', tablefmt='pipe', showindex=False)

        print(tabela_listar)

    def teste(self, nome_produto):
         if nome_produto:
            for prod in self.loja.prod_loja:
                if prod.produto == nome_produto:
                    return prod
            return None