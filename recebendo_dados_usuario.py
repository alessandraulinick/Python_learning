#Entrada de dados

print("Nome: ")
nome=input() #input -> entrada

idade=int(input("Idade: "))

#processamento

#Saídas de dados
print("A %s tem %d anos" %(nome, idade))
print("A {0} tem {1} anos".format(nome, idade))
print(f"A {nome} tem {idade} anos")

print(f"A {nome} nasceu em {2021-idade}")