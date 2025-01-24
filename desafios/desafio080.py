print("========== DESAFIO 80 =========")

listanum = list()

for c in range(0, 5):
    n = int(input("Digite um valor: "))
    # Daqui pra baixo tá substituindo o sort()
    if c == 0 or n > listanum[-1]:
        listanum.append(n)
        print("Valor adicionado ao final da lista.")
    else:
        posi = 0
        while posi < len(listanum):
            if n <= listanum[posi]:
                listanum.insert(posi, n)
                print(f"Valor adicionado na posição: {posi} da lista.")
                break
            posi += 1

print("=-" * 30)
print(f"Você digitou: {listanum}")
print("=-" * 30)
print("FIM DO CODIGO")
