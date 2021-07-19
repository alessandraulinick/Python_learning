#listas
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['g', 'c', 'e', 'k', ' ', 'u', 'n', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('alessandra ulinick')

#Utilizar variaveis
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

#checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o numero {num} da lista 4\n')
else:
    print(f'Não encontrei o numero {num} da lista 4\n') 

letra = 'e'
if letra in lista5:
    print(f'Encontrei a letra {letra} da lista 5\n')
else:
    print(f'Não encontrei a letra {letra} da lista 5\n')

#ordenar uma lista
lista1.sort()
print(f'Lista 1 ordenada: {lista1}\n')

lista2.sort()
print(f'Lista 2 ordenada {lista2}\n')

lista5.sort()
print(f'Lista 5 ordenada {lista5}\n')

#conta quantos numeros 1 tem na lista 1
print(lista1.count(1))

#conta quantas letras "a" tem na lista 5
print(lista5.count('a'))

#Adicionar elementos em listas
#Para add elementos em listas, usamos a função append
#com append só se adiciona um elemento por vez
print(lista1)
lista1.append(42)
print(lista1)

#Adiciona a lista como uma sublista, elemento unico
lista1.append([8, 3, 1])
print(lista1)
if [8, 3, 1] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

#Adicionar mais elementos de uma unica vez, adiciona um a um, não é uma sublista
#Não aceita valor único
lista1.extend([123, 44, 67])
print(f'Lista 1 {lista1}')


