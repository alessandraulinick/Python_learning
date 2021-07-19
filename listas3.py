type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['g', 'c', 'e', 'k', ' ', 'u', 'n', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('alessandra ulinick')

#Converter string para uma lista
#Exemplo 1
nome = 'Alessandra Ulinick'
print(f'String: {nome}')
#Split separa os elementos da lista pelo espaço entre elas
nome = nome.split()
print(f'String como lista: {nome}\n')

#Exemplo 2
nome2 = 'Alessandra,Ulinick'
print(f'String: {nome2}')
#Split separando os elementos separados por virgulas
nome2 = nome2.split(',')
print(f'String como lista: {nome2}')

#Converter lista em string
nome3 = ['Alessandra', 'Ulinick']
print(f'Lista: {nome3}')
#Join converte a lista em string e separa os elementos ' ' por um espaço
nome3 = ' '.join(nome3)
print(f'Lista convertida em String: {nome3}')