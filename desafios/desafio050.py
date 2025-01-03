print("========== DESAFIO 50 =========")

soma = 0
cont = 0

for c in range(1, 7):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print("A soma de todos os {} número pares digitados é igual a: {}.".format(cont, soma))

print("-=" * 15)
print("FIM DO CODIGO")
