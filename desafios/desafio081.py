
print("========== DESAFIO 81 =========")

lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))

    parar = " "
    while parar not in "SN":
        parar = str(input("Deseja continuar [S/N]?: ")).upper().strip()[0]

    if parar in "Nn":
        break

print("=-" * 30)
print(f"Foram ditados {len(lista)} elementos")
print(f"Os valores em ordem cresente são: {(sorted(lista))}")
lista.sort(reverse=True)
print(f"Os valores em ordem decresente são: {lista}")
if 5 in lista:
    print("O valor 5 ESTÁ na lista")
else:
    print("O valor 5 NÃO está na lista")
print("=-" * 30)
print("FIM DO CODIGO")