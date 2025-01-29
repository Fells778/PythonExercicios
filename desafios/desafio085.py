print("========== DESAFIO 85 =========")

listanum = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f"Digite o {c}° valor: "))
    if valor % 2 == 0:
        listanum[0].append(valor)
    elif valor % 2 == 1:
        listanum[1].append(valor)

print("=-" * 30)
print(f"Lista completa: {listanum}.")
print(f"Lista de números pares: {sorted(listanum[0])}")
print(f"Lista de números ímpares: {sorted(listanum[1])}")
print("=-" * 30)
print("FIM DO CODIGO")