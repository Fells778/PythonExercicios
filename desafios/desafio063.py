print("========== DESAFIO 63 =========")

print("Sequência de Fibonacci...")
print("=-" * 20)
n = int(input("Digite quantos termos você quer mostrar: "))
termo01 = 0
termo02 = 1
cont = 3
print("{} -> {}".format(termo01, termo02), end="")

while cont <= n:
    termo3 = termo01 + termo02
    print(" -> {}".format(termo3), end="")
    termo01 = termo02
    termo02 = termo3
    cont += 1

print("-> FIM!")
print("=-" * 20)
print("FIM DO CODIGO")