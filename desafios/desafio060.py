from math import factorial
print("========== DESAFIO 60 =========")

num = int(input("Digite um número: "))
# fac = factorial(num)
c = num
fac = 1
print("Calculando o fatorial de {}! ". format(num))
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    fac *= c
    c -= 1
print("{}.".format(fac))

print("=-" * 20)
print("FIM DO CODIGO")
