print("========== DESAFIO 43 =========")

peso = float(input("Informe seu peso (Kg): "))
altura = float(input("Informe sua altura (m): "))

calculo = peso / (altura ** 2)

if calculo < 18.5:
    print("Seu índice de massa corporal é de {:.1f}".format(calculo))
    print("Abaixo do peso!")
elif 18.5 <= calculo < 25:
    print("Seu índice de massa corporal é de {:.1f}".format(calculo))
    print("Peso ideal!")
elif 25 <= calculo < 30:
    print("Seu índice de massa corporal é de {:.1f}".format(calculo))
    print("Sobrepeso!")
elif 30 <= calculo < 40:
    print("Seu índice de massa corporal é de {:.1f}".format(calculo))
    print("Obesidade!")
else:
    print("Seu índice de massa corporal é de {:.1f}".format(calculo))
    print("Cuidado! Obesidade mórbida!")

print("-=" * 15)
print("FIM DO CODIGO")