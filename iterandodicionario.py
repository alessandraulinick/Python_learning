receita = {'jan': 100, 'fev': 120, 'mar': 300}

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita.keys(): #Recomendado
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi RS{receita[chave]}')
print('\n')
#Acessando as chaves
print(receita.keys()) #Acesso a todas as chaves sem precisar do for

#Acessando os valores
print(receita.values())
for valor in receita.values():
    print(valor)


