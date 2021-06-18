numero = float(input("Digite seu primeiro número: "))
numero_dois = float(input("Digite seu segundo número: "))

if numero>numero_dois:
    print(f"O maior número é: {numero}")
elif numero<numero_dois:
    print(f"O maior número é: {numero_dois}")
else:
    print("Eles são iguais")