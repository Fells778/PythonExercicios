import random
from time import sleep

print("========== DESAFIO 45 =========")
print("========== PEDRA, PAPEL E TESOURA ============")
print("Escolha uma das opções abaixo:")
print("[0] - Pedra")
print("[1] - Papel")
print("[2] - Tesoura")

itens = ["Pedra", "Papel", "Tesoura"]

escolhaJogador = int(input("Sua jogada: "))
pc = random.randint(0,2)

print("=-" * 10)
sleep(0.3)
print("\033[4:34mPEDRA\033[m")
sleep(0.3)
print("\033[4:36mPAPEL\033[m")
sleep(0.3)
print("\033[4:34mTesoura!!!\033[m")
sleep(0.5)
print("=-" * 10)

if escolhaJogador == pc:
    print("\033[4:32mEmpate, ambos escolheram {}!\033[m".format(itens[escolhaJogador]))
elif escolhaJogador != pc:
    escolhaPC = itens[pc]
    jogada = itens[escolhaJogador]
    if jogada == "Pedra" and escolhaPC == "Papel":
        print("\033[4:35mO computador venceu:\033[m {} ganha de {}.".format(escolhaPC, jogada))
    elif jogada == "Papel" and escolhaPC == "Tesoura":
        print("\033[4:35mO computador venceu:\033[m {} ganha de {}.".format(escolhaPC, jogada))
    elif jogada == "Tesoura" and escolhaPC == "Pedra":
        print("\033[4:35mO computador venceu:\033[m {} ganha de {}.".format(escolhaPC, jogada))
    else:
        print("\033[4:32mParabéns! Você ganhou:\033[m {} vence {}".format(jogada, escolhaPC))
else:
    print("Opção invalida! Tente novamente.")

# Outra forma:

# jogada = int(input("Sua jogada: "))
# lista = ["Pedra", "Papel", "Tesoura"]
# pc = random.choice(lista)
# if jogada == 1:
#     escolha = "Pedra"
#     if escolha == "Pedra" and pc == "Papel":
#         print("Papel ganhou")
#     elif escolha == "Papel" and pc == "Tesoura":
#         print("Tesoura ganhou")
#     elif escolha == "Tesoura" and pc == "Pedra":
#         print("Pedra ganhou")
#     else:
#         print("{} ganhou de {}".format(escolha, pc))
#     if pc == escolha:
#         print("Emapte!\nVocê escolheu {} e o computador {}.".format(escolha, pc))
# elif jogada == 2:
#     escolha = "Papel"
#     if escolha == "Pedra" and pc == "Papel":
#         print("Papel ganhou")
#     elif escolha == "Papel" and pc == "Tesoura":
#         print("Tesoura ganhou")
#     elif escolha == "Tesoura" and pc == "Pedra":
#         print("Pedra ganhou")
#     else:
#         print("{} ganhou de {}".format(escolha, pc))
#     if pc == escolha:
#         print("Emapte\n Você escolheu {} e o computador {}.".format(escolha, pc))
# elif jogada == 3:
#     escolha = "Tesoura"
#     if escolha == "Pedra" and pc == "Papel":
#         print("Papel ganhou")
#     elif escolha == "Papel" and pc == "Tesoura":
#         print("Tesoura ganhou")
#     elif escolha == "Tesoura" and pc == "Pedra":
#         print("Pedra ganhou")
#     else:
#         print("{} ganhou de {}".format(escolha, pc))
#     if pc == escolha:
#         print("Emapte\n Você escolheu {} e o computador {}.".format(escolha, pc))
# else:
#     print("Digite uma das opções! Tente novamente.")

print("-=" * 15)
print("FIM DO CODIGO")