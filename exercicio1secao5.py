numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite outro valor: "))

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
elif numero1 < numero2:
    print(f'{numero1} é menor que {numero2}')
else:
    print(f'{numero1} é igual a {numero2}')