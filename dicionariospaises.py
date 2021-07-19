#Criação de dicionarios
#Forma 1 - mais comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(f'Forma 1: {paises}')

#Forma 2 - menos comum
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(f'Forma 2: {paises}')

#Acessando elementos
#Forma 1 - Acessando via chave da mesma forma que lista/tupla
print(paises['br']) 

#Forma 2 - Acessando via get (Recomendado)
print(paises.get('br'))

pais = paises.get('py')
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei país')

pais = paises.get('ru', 'Não encontrado') #Substirui o if/else
print(f'Encontrei o país {pais}')

#Verificar elementos
print('br' in paises) 
print('Estados Unidos' in paises) #Busca sempre pela chave e nunca pelo valor
