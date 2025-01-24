from time import sleep

print("========== DESAFIO 79 =========")

listanum = []
while True:
    n = int(input("Digite um valor: "))
    if n not in listanum:
        listanum.append(n)
        print("Valor adicionado com sucesso...")
        sleep(0.2)
    else:
        print("Valor duplicado, não vai adicionado!")
        print("=-=" * 15)

    parar = " "
    while parar not in "SN":
        parar = str(input("Deseja continuar [S/N]:? ")).strip().upper()[0]

    if parar in "Nn":
        break
        
print("=-" * 30)
print(f"Você digitou: {sorted(listanum)}")
print("=-" * 30)
print("FIM DO CODIGO")
