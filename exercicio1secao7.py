type([])

A = [1, 0, 5, -2, -5, 7]

soma = A[0]+A[1]+A[5]

print(f'Soma = {soma}')

for indice, B in enumerate(A):
    print(f'O numero {B} está no indice {indice}')

A.pop(4)
A.insert(4, 100)
print(A)

for i in A:
    print(f'Valor: {i}')
    