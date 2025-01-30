print("========== DESAFIO 87 =========")
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maiorvalor = somacolona = 0
# Esse for alimenta...
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor {[linha]}, {[coluna]}: "))
print("=-" * 30)
# E esse for formata e mostra na tela...
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
        # verifica quais são os pares e soma eles...
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
print("=-" * 30)
print(f"A soma de todos os valores pares da matriz é: {somapar}.")
# soma os elementos da 3° coluna (coluna fixa e linha variavel)...
for linha in range(0, 3):
    somacolona += matriz[linha][2]
print(f"A soma dos valores da 3° coluna é: {somacolona}.")
# Verifica o maior valor da 2° linha da matriz...
for coluna in range(0, 3):
    if coluna == 0:
        maiorvalor = matriz[1][coluna]
    elif matriz[1][coluna] > maiorvalor:
        maiorvalor = matriz[1][coluna]
print(f"O maior valor da 2° linha é: {maiorvalor}.")
print("=-" * 30)
print("FIM DO CODIGO")
