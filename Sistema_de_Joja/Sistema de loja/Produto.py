class Produto:
    def __init__(self, produto, preco, quantidade_estoque):
        self.produto = produto
        self.preco = preco
        self.qtd_estoque = quantidade_estoque

    
    def mostrar_produto(self):
        return f'Nome: {self.produto}\nPreço: {self.preco}\nQuantidade Produto: {self.qtd_estoque}'
