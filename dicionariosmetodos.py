d = dict(a=1, b=2, c=3)
print(d)

#copiando um dicionario para outro - deep copy
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

#copiando um dicionario para outro - Shallow Copy
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)

#Limpar dicionario - zerar dados
d.clear()
print(d)

#Forma não usual de criar dicionarios
#metodo fromkeys recebe dois parametros: um iteravel e um valor
outro = {}.fromkeys('teste', 'valor')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

#Desempacotamento de dicionarios
receita = {'jan': 100, 'fev': 120, 'mar': 300}
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

#Soma, Valor Maximo, Valor Minimo - Apenas valores Inteiros ou reais
print(f'Soma: {sum(receita.values())}')
print(f'Maximo: {max(receita.values())}')
print(f'Mínimo: {min(receita.values())}')

#Tamanho dicionarios
print(f'Tamanho: {len(receita)}')