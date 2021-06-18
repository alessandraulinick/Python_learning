import math

numero = float(input("Digite seu numero: "))

if numero>0:
    print(f"A raiz quadrada é: {math.sqrt(numero)}")
else:
    print(f"Não é possível calcular a raiz de {numero}")
