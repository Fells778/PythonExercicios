print("====== DESAFIO 034 =======")

salario = float(input("Por favor informe seu salario: "))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
    print("Seu antigo salário de R${:.2f}".format(salario))
    print("Agora é R${:.2f} por mês, com aumento de 15%!".format(aumento))
else:
    aumento = salario + (salario * 10 / 100)
    print("Seu antigo salário de R${:.2f}".format(salario))
    print("Agora é R${:.2f} por mês, com aumento de 10%!".format(aumento))

print("=" * 20)
print("Tenha um otimo mês!")

print("====== FIM DO CODIGO =========")
