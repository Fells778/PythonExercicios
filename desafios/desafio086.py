print("========== DESAFIO 86 =========")
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Esse for alimenta...
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor {[linha]}, {[coluna]}: "))
print("=-" * 30)
# E esse for formata e mostra na tela...
for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()

print("=-" * 30)
print("FIM DO CODIGO")
