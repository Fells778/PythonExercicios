from random import randint

print("========== DESAFIO 68 =========")

while True:
    print("=-" * 20)
    n = int(input("Digte um valor: "))
    escolha = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()
    print("=-" * 20)
    n_pc = randint(0, 10)
    soma = n + n_pc
    print(f"Você jogou {n} e o computador {n_pc}.")
    print(f"{n} + {n_pc} = {soma}.")

    if escolha in "Pp":
        if n % 2 == 0:
            print(f"{soma} é PAR, você venceu!")
        else:
            print(f"{soma} é ÍMPAR, você perdeu!")
            break
    elif escolha in "Ii":
        if n % 2 == 1:
            print(f"{soma} é ÍMPAR, você venceu!")
        else:
            print(f"{soma} é PAR, você perdeu!")
            break
    else:
        print("Opção invalida, tente novamente!")
print("=-" * 20)
print("FIM DO CODIGO")
