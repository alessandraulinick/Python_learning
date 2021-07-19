type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['g', 'c', 'e', 'k', ' ', 'u', 'n', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('alessandra ulinick')

#Podemos inserir um elemento na lista informando a posição do índice
#Nao substitui nenhum valor, apenas desloca os elementos
lista1.insert(2, 77)
lista1.sort()
print(f'Lista 1 {lista1}')

#juntar duas listas
lista6 = lista1 + lista4
print(f'Lista 6 {lista6}')

#lista inversa
lista1.reverse()
print(f'Lista 1 reversa {lista1}')

#copiar uma lista
lista7 = lista4.copy()
print(f'Lista 7 {lista7}')

#Quantidade de elemetos de uma lista
print(f'Tamanho lista 5: {len(lista5)} elementos')

#Remover o ultimo elemento de uma lista
#Retorna o ultimo elemento que vai remover
lista5.pop()
print(f'Remover o ultimo elemento {lista5}')

#Remover elemento pelo indice
#Se não houver elemento no indice informado ele vai dar erro
lista5.pop(0)
print(f'Remover o elemento 0: {lista5}')

#Remover todos os elementos (Zerar lista)
lista5.clear()
print(f'Lista 5 limpa: {lista5}')

#Repetir elementos de uma lista
nova = [1, 2, 3]
nova = nova*3
print(nova)