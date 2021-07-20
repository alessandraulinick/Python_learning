#definindo um set (conjunto)

#Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) #Não é permitido valores duplicados
print(s) #valores duplicados  serao ignorados

#Forma 2 - mais comum
s = {1, 2, 3, 4, 5, 6, 7, 2, 3}
print(s)

#verificar se o elemento esta na funcao
if 3 in s:
    print('sim')
else:
    print('nao')

#Remover Forma 1
s1 = {1, 2, 3}
s1.remove(3) #informa o valor a ser removido
print(s1)

#Remover Forma 2
s1 = {1, 2, 3}
s1.discard(1) #informa o valor a ser removido
print(s1)

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

#gerar conjuntos com nomes dos estudantes únicos
#Forma 1
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

#Forma 2
unicos2 = estudantes_java | estudantes_python #caractere pipe (|)
print(unicos2)

#Gerar conjunto de nomes que estão em ambos conjuntos
#Forma 1
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#Forma2
ambos2 = estudantes_java & estudantes_python
print(ambos2)

#Gerar conjunto de estudantes de um curso q não esta em outro
so_python = estudantes_python.difference(estudantes_java)
print(f'So python {so_python}')
so_java = estudantes_java.difference(estudantes_python)
print(f'So java {so_java}')

#Soma, Valor Maximo, Valor Minimo - Apenas valores Inteiros ou reais
s3 = {1, 2, 3, 4, 5, 6}
print(f'Soma: {sum(s3)}')
print(f'Maximo: {max(s3)}')
print(f'Mínimo: {min(s3)}')

#Tamanho tupla
print(f'Tamanho: {len(s3)}')