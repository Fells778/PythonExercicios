from time import sleep

print("========== DESAFIO 67 =========")

while True:
    print("=-" * 20)
    n = int(input("Digite um número para ver sua tabuada: "))
    print("=-" * 20)
    if n < 0:
        print("Você digitou um número negativo, tente novamente!")
        break
    for c in range(1, 11):
        multi = c * n
        print(f"{n} x {c} = {multi}.")
        sleep(0.25)

print("=-" * 20)
print("FIM DO CODIGO")
