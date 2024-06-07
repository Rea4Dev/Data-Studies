#Declarações
valores = []
count = 0
for i in range(0, 9):
    valores.append([])

#Entrada de valores
for i in range(0, 9):
    valores[i].append(int(input(f"Digite o valor: ")))

#Saída
for i in range(0, 9):
    if count == 0:
        print(valores[i], end=" ")
    elif count % 3 != 0:
        print(valores[i], end=" ")
    else:
        print()
    count += 1