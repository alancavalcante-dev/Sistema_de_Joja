from tabulate import tabulate
import pandas as pd

class Loja:
    def __init__(self):
        self.prod_loja = []
        self.lista_de_clientes = []
        
    def adicionar_produto(self, produto):
        self.prod_loja.append(produto)

    def remover_produto(self, nome_produto):
        for produto in self.prod_loja:
            if produto.produto == nome_produto:
                self.prod_loja.remove(produto)
                print(f'Produto "{nome_produto}" removido da loja.')
                return
        print(f'Produto "{nome_produto}" não encontrado na loja.')
        
    def listar_produtos_da_loja(self, nome_produto=False):  
        # Convertendo a lista de produtos para um DataFrame
        self.df_produtos = pd.DataFrame([vars(produto) for produto in self.prod_loja])
        
        # Usando tabulate para formatar a tabela
        tabela_listar = tabulate(self.df_produtos, headers='keys', tablefmt='pipe', showindex=False)

        print(tabela_listar)

        

