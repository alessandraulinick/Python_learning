type([])

#Copiando uma lista para outra (Deep Copy)
lista = [1, 2, 3]
nova = lista.copy()
print(f'Lista: {lista}')
print(f'Nova: {nova}')
#As listas ficartam totalmente independentes, ou seja, se eu modificar a lista nova
#não vai ser alterado nada da lista original
nova.append(4)
print(f'Lista: {lista}')
print(f'Nova: {nova}')

#Copiando uma lista para outra (Shallow Copy)
lista2 = [1, 2, 3]
nova2 = lista2
print(f'Lista 2: {lista2}')
print(f'Nova 2: {nova2}')
#As modificações irão refletir em ambas as listas, se modificar uma a outra tambem sera modificada
nova2.append(4)
print(f'Lista: {lista2}')
print(f'Nova: {nova2}')