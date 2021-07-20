type([])

#Slice de lista com parametro 'inicio'
lista = [1, 2, 3, 4]
print(lista[1:]) #inciando no indice 1 e passando por todos os elementos

#Slice de lista com parametro 'fim'
print(lista[:3])

#Slice de lista com parametro 'inicio' e 'fim'
print(lista[1:3])

#Slice de lista com parametro 'passo'
print(lista[::2]) #comeca em 0 e vai até o final de 2 em 2
print(lista[1::2]) #comeca em 1 e vai até o final de 2 em 2

lista.reverse()
print(lista)

#Soma, valormaximo, valorminino - valores inteiros apenas
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Soma: {sum(lista2)}')
print(f'Minimo: {min(lista2)}')
print(f'Maximo: {max(lista2)}')
#Tamanho da lista
print(f'Tamanho: {len(lista2)}')

#Transformar lista em tupla
tupla = tuple(lista2)
print(f'tupla:  {tupla}')