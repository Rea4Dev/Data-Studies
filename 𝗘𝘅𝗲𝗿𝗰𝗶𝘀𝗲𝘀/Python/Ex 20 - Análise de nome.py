nome = input("Insira o nome completo: ")

#Elimina os espaços e transfrma em maiúscula
print(nome.strip().upper())

#Elimina os espaços e transforma em minúscula
print(nome.strip().lower())

#Tamanho da string sem os espaços
print(len(nome.strip()))

#Tamanho do primeiro nome
nome = nome.split()
print(len(nome[0]))