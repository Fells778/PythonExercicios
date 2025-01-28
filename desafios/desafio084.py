print("========== DESAFIO 84 =========")

pessoas = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()

    parar = " "
    while parar not in "SN":
        parar = str(input("Deseja parar [S/N]?: ")).upper().strip()[0]

    if parar in "Nn":
        break
    dado.clear()

print("=-" * 30)
print(f"Lista: {pessoas}")
print(f"No total foram digitados {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maior}kg. Peso de ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]}", end="")
print()
print(f"O menor peso foi de {menor}kg. Peso de ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f"{p[0]}", end="")
print()
print("=-" * 30)
print("FIM DO CODIGO")