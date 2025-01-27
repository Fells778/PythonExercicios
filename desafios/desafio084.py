print("========== DESAFIO 84 =========")

pessoas = list()
dado = list()
cont = 0

while True:
    dado.append(str(input("Nome: ")))
    dado.append(str(input("Peso: ")))
    pessoas.append(dado[:])
    cont += 1

    parar = " "
    while parar not in "SN":
        parar = str(input("Deseja parar [S/N]?: ")).upper().strip()[0]

    if parar in "Nn":
        break
    dado.clear()

print("=-" * 30)
print(f"No total foram digitados {cont} pessoas.")
print(f"O maior peso foi de {max(pessoas[1])}kg. Peso de {pessoas[0]}")
print(f"O menor peso foi de {min(pessoas[1])}kg. Peso de {pessoas[0]}")
print("=-" * 30)
print("FIM DO CODIGO")