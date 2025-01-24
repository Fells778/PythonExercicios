print("========== DESAFIO 81 =========")

lista = list()
listaPar = list()
listaImpa = list()

while True:
    # Add o valor na lista...
    lista.append(int(input("Digite um número: ")))

    # Verifica se quer parar...
    parar = " "
    while parar not in "SN":
        parar = str(input("Deseja continuar [S/N]?: ")).upper().strip()[0]
    # Para o codigo...
    if parar in "Nn":
        break
# Verifica qual é impar e par...
for i, v in enumerate(lista):
    if v % 2 == 0:
         listaPar.append(v)
    elif v % 2 == 1:
        listaImpa.append(v)

print("=-" * 30)
# Mostra a lista completa...
print(f"Lista completa: {lista}.")
# Mostra a lista de pares..
print(F"Lista de números pares: {listaPar}.")
# Mostra a lista de impares...
print(f"Lista de números ímpares: {listaImpa}")
print("=-" * 30)
print("FIM DO CODIGO")