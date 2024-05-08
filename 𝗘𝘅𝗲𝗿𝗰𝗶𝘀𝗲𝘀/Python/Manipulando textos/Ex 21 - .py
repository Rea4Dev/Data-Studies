# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = input("Digite o número até 9999: ")
numSplited = num.split()

print(f"O número digitado foi: {num}.\nMilhar: {numSplited[0][0]}\nCentena: {numSplited[0][1]}\nDezena: {numSplited[0][2]}\nUnidade: {numSplited[0][3]}")