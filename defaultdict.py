dicionario = {'curso': 'Programacao em python'}
print(dicionario['curso'])

#Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programacao em python'
print(dicionario)
