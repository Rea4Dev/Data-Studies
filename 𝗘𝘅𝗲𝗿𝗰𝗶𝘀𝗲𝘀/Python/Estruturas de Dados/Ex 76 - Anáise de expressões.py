# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = input('Digite a expressão: ')
abre = 0
fecha = 0
for i in expressao:
    if i == "(":
        abre += 1
    elif i == ")":
        fecha += 1
if abre==fecha:
    print("Certo")
else:
    print("Errado")