print("========== DESAFIO 36 =========")

casa = float(input("Informe o valor da casa: R$ "))
salario = float(input("Informe o salário do comprador: R$ "))
anos = int(input("Quantos anos de financiamento?: "))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print("Para pagar a casa no valor de R${:.2f} em {} anos".format(casa, anos))
print("A prestação será de R${:.2f}".format(prestacao))
if prestacao > minimo:
    print("Esse financiamento \033[4:31mNÃO FOI APROVADO!\033[m")
else:
    print("Esse financiamento \033[4:32mFOI APROVADO!\033[m")
print("-=" * 15)
print("FIM DO CODIGO")