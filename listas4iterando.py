type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('alessandra ulinick')

#iterando sobte listas
#Exemplo 1 - for nm
soma = 0
for elemento in lista1:
    lista1.sort()
    print(f'Elemento lista 1: {elemento}')
    soma = soma + elemento
print(f'A soma dos elementos da lista 1 é: {soma}')

#Exemplo 2 - for string
soma2 = ''
for elemento2 in lista2:
    print(f'Elemento lista 2: {elemento2}')
    soma2 = soma2 + elemento2
print(f'A soma dos elementos da lista 2 é: {soma2}')

#Exepmlo 3 - while
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione produtos na lista ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(f'Produtos: {produto}')
 
