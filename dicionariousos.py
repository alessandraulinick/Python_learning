#Lista para carrinhos
#Teria que saber qual é o indice de cada informação no produto
carrinho = []
produto1 = ['Playstation', 1, 2300.00]
produto2 = ['Jogo', 1, 100.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#Tupla para carrinhos
#Teria que saber qual é o indice de cada informação no produto
carrinho = []
produto1 = ('Playstation', 1, 2300.00)
produto2 = ('Jogo', 1, 100.00)
carrinho = (produto1, produto2)
print(carrinho)

#Dicionario para carrinhos
#Mwlhor para essa utilização
carrinho = []
produto1 =  {'nome': 'Playstation', 'quantidade': 1, 'preco': 2300.00}
produto2 =  {'nome': 'Playstation', 'quantidade': 1, 'preco': 2300.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
