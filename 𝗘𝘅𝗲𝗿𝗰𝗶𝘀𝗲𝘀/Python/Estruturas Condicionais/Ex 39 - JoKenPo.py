from random import randint

escolhaUser = int(input("""
Escolha (1) para pedra.
Escolha (2) para papel.
Escolha (3) para tesoura.
"""))
escolhaPc = randint(1, 3)

if escolhaPc == 1:
    if escolhaUser == 2:
        print(f"Pc escolheu {escolhaPc}.")
        print("Você ganhou.")
    elif escolhaUser == 1:
        print(f"Pc escolheu {escolhaPc}.")
        print("Empate.")
    else:
        print(f"Pc escolheu {escolhaPc}.")
        print("Você perdeu.")

if escolhaPc == 2:
    if escolhaUser == 3:
        print(f"Pc escolheu {escolhaPc}.")
        print("Você ganhou.")
    elif escolhaUser == 2:
        print(f"Pc escolheu {escolhaPc}.")
        print("Empate.")
    else:
        print(f"Pc escolheu {escolhaPc}.")
        print("Você perdeu.")

if escolhaPc == 3:
    if escolhaUser == 1:
        print(f"Pc escolheu {escolhaPc}.")
        print("Você ganhou.")
    elif escolhaUser == 3:
        print(f"Pc escolheu {escolhaPc}.")
        print("Empate.")
    else:
        print(f"Pc escolheu {escolhaPc}.")
        print("Você perdeu.")