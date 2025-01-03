print("====== DESAFIO 033 =======")

print("Digite 3 núemros")
num01 = float(input("Primeiro número: "))
num02 = float(input("Segundo número: "))
num03 = float(input("Terceiro número: "))
# Verifica o menor numero...
menor = num01
if num02 < num01 and num02 < num03:
    menor = num02
if num03 < num01 and num03 < num02:
    menor = num03
# Verifica o maior numero...
maior = num01
if num02>num01 and num02 > num03:
    maior = num02
if num03 > num01 and num03 > num02:
    maior = num03
print("=" * 20)
print("O menor número digitado foi: {}.".format(menor))
print("O maior número digitado foi: {}.".format(maior))

print("====== FIM DO CODIGO =========")
