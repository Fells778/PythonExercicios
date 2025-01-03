print("========== DESAFIO 55 =========")
pesoMaior = 0
pesoMenor = 0
for c in range(1, 3):
    peso = float(input("Digite o peso da {}° pessoa: ".format(c)))
    if c == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        elif peso < pesoMenor:
            pesoMenor = peso
print("-=" * 15)
print("O maior peso foi: {}Kg.".format(pesoMaior))
print("O menor peso foi: {}Kg.".format(pesoMenor))
print("-=" * 15)
print("FIM DO CODIGO")