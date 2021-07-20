#Utilizar counter - import counter
from collections import Counter
from functools import partial

lista = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 5, 5, 5, 5, 3, 45, 66, 43, 34 ]

#utilizando o counter
#Exemplo 1
res = Counter(lista)
print(res) #Para cada elemento da lista o counter criou uma chave e colocou como valor a qtdd de ocorrencias

#Exemplo 2
print(Counter('Alessandra Ulinick'))

#Exemplo 3
texto = """San Holo taocava em bandas com amigos e ensinav crianças a tocar guitarra
o próprio estudou o instrumento na universidade Codarts. Decidiu seguir produzindo 
canções para outros artistas sem levar crédito (conhecido como ghost producing), 
o que teve sucesso considerável, levando-o a seguir uma carreira solo. 
Sua carreira começou lançando os extended plays (EPs) Corellia e Demons em 2013."""
palavras = texto.split()
res1 = Counter(palavras)
print(res1)
