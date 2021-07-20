tupla = (1, 2, 3)
for n in tupla:
    print(f'Valor: {n}')

for indice, valor in enumerate(tupla):
    print(f'Indice: {indice} - valor: {valor}')

meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
i = 0
while i < len(meses):
    print(meses[i])
    i = i +1
