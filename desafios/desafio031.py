print("====== DESAFIO 031 =======")

distancia = float(input("Digite a distancia da viagem: "))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print("O valor da passagem é de R${:.2f} reais.".format(passagem))
print("Tenha uma otima viagem!")

print("====== FIM DO CODIGO =========")