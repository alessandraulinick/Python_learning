i = 0
n = int(input("Digite um nm inteiro positivo: "))

if n > 0:
    while i < n:
        i = i + 1
        if (i % 2 == 0):
            print(f'Par: {i}')
        else:
            print(f'Impar: {i}')

print("\nLaço For")
for i in range(n):
    i = i + 1
    if (i % 2 == 0):
        print(f'Par: {i}')
    else:
        print(f'Impar: {i}')
