from tabulate import tabulate
import pandas as pd

class Loja:

    def __init__(self):
        self.prod_loja = []
        self.lista_de_clientes = []
        self.numero_de_produtos = len(self.prod_loja)
        

    def adicionar_produto(self, produto):
        self.prod_loja.append(produto)


    def remover_produto(self, nome_produto):
        for produto in self.prod_loja:
            if produto.produto == nome_produto:
                self.prod_loja.remove(produto)
                print(f'Produto "{nome_produto}" removido da loja.')
                return
        print(f'Produto "{nome_produto}" não encontrado na loja.')
        
    
    def listar_estoque(self):
        df_table = pd.DataFrame([{'produto': item.produto, 'preco': item.preco, 'qtd_produto': item.qtd_estoque} for item in self.prod_loja])
        tabela_formatada = tabulate(df_table, headers=['Id','Produto','Preço','Qtd produto'], tablefmt="pipe")
        return tabela_formatada