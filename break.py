#Exemplo 1 

for num in range(1, 11):
    if num == 6: 
        break
    else:
        print(num)

print('Sai loop')

#Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break