print("====== DESAFIO 029 =======")

velocidade = float(input("Digite a velociade atual do seu carro: "))
if velocidade > 80:
    print("{:.1f}Km/h, chefe? Você foi multado!".format(velocidade))
    multa = (velocidade - 80) * 7
    print("O valor da multa é de: R${:.2f} reais.".format(multa))
else:
    print("Está dentro do limite de velocidade. Siga em frente!")
print("Lembrete: Respeite as leis de transito e dirija com resposabilidade!")

print("====== FIM DO CODIGO =========")