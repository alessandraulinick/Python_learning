#Adicionar elementos em um dicionario
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

#Forma1 - Mais comum
receita['abr'] = 350
print(receita)

#Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

#Atualizar dados
#Forma 1
receita['mai'] = 550
print(receita)

#Forma 2
receita.update({'mai': 600})
print(receita)

#Remover dados
#Forma 1 - Mais comum
ret = receita.pop('mar') #Informar sempre a chave
print(ret) #Remove e retorna o valor
print(receita)

#Forma 2
del receita['fev'] #Nesse caso o valor removido não é recuperado
print(receita)

