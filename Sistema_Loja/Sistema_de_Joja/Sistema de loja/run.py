from Cliente import Cliente
from Loja import Loja
from Produto import Produto
from Carrinho import Carrinho

# Criando loja
loja1 = Loja()

# Criando produtos
tenis_nike_shox = Produto('Nike Shox', 220.45, 3)
tenis_adidas_ultraboost = Produto('Super Star XLG', 150.75, 3)
tenis_puma_suede = Produto('Puma Suede', 250.80, 3)



# Adicionando produtos à loja
loja1.adicionar_produto(tenis_nike_shox)
loja1.adicionar_produto(tenis_adidas_ultraboost)
loja1.adicionar_produto(tenis_puma_suede)
print("Lista do estoque")
print(loja1.listar_estoque())


carrinho = Carrinho(loja1)
carrinho.adicionar_item(tenis_nike_shox, 4)
carrinho.adicionar_item(tenis_adidas_ultraboost, 2)
carrinho.adicionar_item(tenis_puma_suede, 1)

print()
print()
print()
print('Lista do carrinho')
print(carrinho.listar_carrinho())
carrinho.adicionar_item(tenis_puma_suede, 1)
print()
print('Lista do carrinho')

carrinho.devolver_item('Puma Sued')
print(carrinho.listar_carrinho())

# print()
# print()
# print()

# print("Lista do estoque")
# print(loja1.listar_estoque())

# carrinho.listar_carrinho()
"""
print(carrinho.lista_de_produtos)
"""
