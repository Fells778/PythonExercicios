from datetime import date
print("========== DESAFIO 54 =========")
ano = 0
contMaior = 0
contMenor = 0
for c in range(1, 8):
    ano = int(input("Digite em que ano a {} pessoa nasceu?: ".format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        contMaior += 1
    else:
        contMenor += 1
print("No total temos {} pesosas maiores de idade.".format(contMaior))
print("E no total temos {} pesosas menores de idade".format(contMenor))
print("-=" * 15)
print("FIM DO CODIGO")