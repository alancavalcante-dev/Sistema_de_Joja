from Cliente import Cliente
from Loja import Loja
from Produto import Produto
from Carrinho import Carrinho

# Criando loja
loja1 = Loja()
loja2 = Loja()
carr2 = Carrinho(loja2)


# Criando produtos
tenis_nike_shox = Produto('Nike Shox', 450.00, 3)
tenis_adidas_ultraboost = Produto('Super Star XLG', 350.00, 3)
tenis_puma_suede = Produto('Puma Suede', 470.00, 3)

# Adicionando produtos à loja
loja1.adicionar_produto(tenis_nike_shox)
loja1.adicionar_produto(tenis_adidas_ultraboost)
loja1.adicionar_produto(tenis_puma_suede)

loja2.adicionar_produto(tenis_puma_suede, 5)
carr2.adicionar_item(tenis_puma_suede)

item1 = Carrinho(loja1)
item1.adicionar_item(tenis_nike_shox, 2)
item1.adicionar_item(tenis_nike_shox, 2)
print(item1.lista_de_produtos)


