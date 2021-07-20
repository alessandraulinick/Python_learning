import math

real = float(input("Número: "))

if real > 0:
    print(f"A raiz de {real} é: {math.sqrt(real)}")
else:
    print(f"O quadrado de {real} é: {real**2}")