class Cliente:
    
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.valor_total = 0


    def pagar_carrinho(self, carrinho) -> bool:
        for prod in carrinho.lista_de_produtos:
            self.valor_total += prod['produto'].preco * prod['qtd_itens']

        if self.saldo >= self.valor_total:
            self.saldo -= self.valor_total
            return True
        else:
            return False

    
