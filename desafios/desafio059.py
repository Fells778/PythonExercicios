print("========== DESAFIO 59 =========")

num01 = int(input("Digite o primeiro valor: "))
num02 = int(input("Segundo valor: "))
escolha = 0

while escolha != 6:
    print("-" * 25)
    print("[1] - Somar")
    print("[2] - Multiplicar")
    print("[3] - Subtração")
    print("[4] - Maior")
    print("[5] - Novos números")
    print("[6] - Sair do programa")
    print("-" * 25)
    escolha = int(input("Informe sua operação: "))
    if escolha == 1:
        soma = num01 + num02
        print("{} + {} = {}.".format(num01, num02, soma))
    elif escolha == 2:
        multi = num01 * num02
        print("{} * {} = {}".format(num01, num02, multi))
    elif escolha == 3:
        sub = num01 - num02
        print("{} - {} = {}".format(num01, num02, sub))
    elif escolha == 4:
        if num01 > num02:
            maior = num01
        else:
            maior = num02
        print("Entre {} e {} o maior valor é {}.".format(num01, num02, maior))
    elif escolha == 5:
        print("Informe os números novamente")
        num01 = int(input("Digite o primeiro valor: "))
        num02 = int(input("Segundo valor: "))
    else:
        escolha = int(input("Digite uma das opções do menu! Tente novamente: "))
print("Saindo do programa!")

print("=-" * 20)
print("FIM DO CODIGO")
