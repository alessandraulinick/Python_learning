import math

nota1 = float(input("Digite sua 1 nota: "))
nota2 = float(input("Digite sua 2 nota: "))

media = (nota1+nota2)/2

if nota1 >=0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    print(f'A media das suas notas é: {media}')
else:
    print("Notas inválidas")