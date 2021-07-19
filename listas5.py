type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['g', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('alessandra ulinick')

#Acesso aos elementos de forma indexada
cores = ['verde', 'amarelo', 'vermelho', 'azul', 'branco']
print(f'Cor na posição 0: {cores[0]}')
print(cores[-1]) #-1 volta a ultima cor, é como se fosse uma roda
for cor in cores:
    print(f'Cor: {cor}')

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

#Gerar indices no for
for indice, cor in enumerate(cores):
    print(f'A cor {cor} está no indice {indice}')

#Encontrar o indice de uma lista
numeros = [5, 6, 7, 5, 8, 9, 10]

#Indice do valor 6
print(f'O valor 6 esta no indice {numeros.index(6)}')

#indice do valor 9
print(f'O valor 9 esta no indice {numeros.index(9)}')

#indice do valor 5
print(f'O valor 5 esta no indice {numeros.index(5)}') #Retorna o indice do primeiro valor encontrado

#busca dentro de um range, qual inidice começar a buscar
print(f'O valor 5 esta no indice {numeros.index(5, 1)}') #buscando a partir o indice 1

#Busca de um range, inicio/fim
print(f'O valor 8 esta no indice {numeros.index(8, 3, 6)}') #busca o indice do valor 8 entre os indices 3 e 6

