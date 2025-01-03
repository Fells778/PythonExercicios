print("========== DESAFIO 38 =========")

num01 = int(input("Digite um número inteiro: "))
num02 = int(input("Digite outro número: "))
if num01 > num02:
    print("O PRIMEIRO valor é maior")
    print("{} é maior que {}.".format(num01, num02))
elif num02 > num01:
    print("O SEGUNDO valor é maior")
    print("{} é maior que {}.".format(num02, num01))
else:
    print("Os dois números são IGUAIS")
print("-=" * 15)
print("FIM DO CODIGO")