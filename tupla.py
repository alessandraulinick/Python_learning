
#Tupla com range
from typing import Tuple


tupla = tuple(range(11))
print(f'tupla: {tupla}')

#Desempacotamento de tupla
tupla1 = ('Geek University', "Alessandra ULinick")
escola, nome = tupla1
print(f'Escola: {escola}')
print(f'Nome: {nome}')

#Soma, Valor Maximo, Valor Minimo - Apenas valores Inteiros ou reais
tupla3 = (1, 2, 3, 4, 5, 6)
print(f'Soma: {sum(tupla3)}')
print(f'Maximo: {max(tupla3)}')
print(f'Mínimo: {min(tupla3)}')

#Tamanho tupla
print(f'Tamanho: {len(tupla3)}')

#Concatenação de tuplas - não altera a tupla original
tupla4 = (1, 2, 3)
tupla5 = (4, 5, 6)
print(f'Concatenar tuplas: {tupla4+tupla5}')

#Concatenação de tuplas - Alterando a tupla original
tupla4 = tupla4 + tupla5
print(f'Concatenação alterando: {tupla4}')

#Verificar se determinado elemento está na tupla
tupla6 = (1, 2, 3, 4, 5, 6)
print(3 in tupla6)

#Contar elementos dentro de uma tupla
tupla7 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla7.count('a')) 

#Acesso de elementos
print(f'Elemento 6 possui o valor: {tupla7[5]}')

#Converter String para tupla
exemplo = tuple('Alessandra Ulinick')
print(exemplo)
print(exemplo.count('e'))

#Qual indice um elemento esta
meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses.index('Setembro'))