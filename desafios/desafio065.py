print("========== DESAFIO 65 =========")

continuar = "S"
soma = quant = media = maior = menor = 0
while continuar in "Ss":
    n = int(input("Digite um número: "))
    soma += n
    quant += 1
    ###
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    ###
    continuar = str(input("Deseja continuar [S/N]?: ")).upper().strip()[0]

media = soma / quant
print("=-" * 20)
print("Você digitou {} números e a media desses números foi {}.".format(quant, media))
print("O maior valor foi {} e o menor foi {}.".format(maior, menor))

print("=-" * 20)
print("FIM DO CODIGO")