print("========== DESAFIO 44 =========")
print("========== LOJINHA: TUDO PELA METADE DO DOBRO ============")

preco = float(input("Informe o valor do produto: R$"))
print("-=" * 15)
print("Escolha a forma de pagamento:")
print("[1] - Á vista Dinheiro/Pix | 10% de desconto")
print("[2] - Á vista no cartão | 5% de desconto")
print("[3] - Em até 2x no cartão | Preço normal")
print("[4] - Em 3x ou mais no cartão | 20% de juros")
print("-=" * 15)
escolha = int(input("Escolha: "))

if escolha == 1:
    total = preco - (preco * 10 / 100)
    print("A vista o valor de {:.2f} fica por {:.2f} com 10% de desconto.".format(preco, total))
elif escolha == 2:
    total = preco - (preco * 5 / 100)
    print("A vista no cartão valor de {:.2f} fica por {:.2f} com 5% de desconto.".format(preco, total))
elif escolha == 3:
    total = preco / 2
    print("Parcelado o valor de R${:.2f} em {}x.".format(preco, total))
elif escolha == 4:
    parcelas = int(input("Em quantas vezes?: "))
    if parcelas < 3:
        print("Só pode parcelar em 3x ou mais vezes")
    else:
        total = preco + (preco * 20 /100)
        parcelas_x = total / parcelas
        print("Parcelado no cartão o valor de R${:.2f} fica por {:.2f} em {}x de  R${:.2f}.".format(preco, total, parcelas, parcelas_x))
else:
    print("Escolha uma das opções validas! Tente novamente.")
print("-=" * 15)
print("FIM DO CODIGO")