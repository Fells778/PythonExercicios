from time import sleep

i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f+1, p):
    print(c)
    sleep(0.3)
print("Fim do código!")

s = 0

for c in range(0, 3):
    n = int(input("Digite um número: "))
    s += n
print("A soma de todos os números é: {}".format(s))
print("Fim do código!")