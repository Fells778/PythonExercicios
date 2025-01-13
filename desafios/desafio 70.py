print("========== DESAFIO 70 =========")

print("=-" * 20)
print("==== LOJA SUPER BARATONA ===")
print("=-" * 20)
prodCaro= prodBarato = 0
while True:
    nome = str(input("Informe o nome do produto: "))
    preco = int(input("Digite o valor do produto: "))

    parar = " "
    while parar not in "SN":
        parar = str(input("Deseja continuar [S/N]:? ")).strip().upper()[0]

    total = preco + preco

    if preco <= 1000:
        prodCaro += 1
    
    if parar in "Nn":
        break

print("=" * 30)
print(f"No total a compra deu: {total:.2f}.")
print(f"Ao todo temos {prodCaro} custando mais de 1000,00.")
print(f"E o prudto mais barato foi {nome} e custa: {prodBarato}")

print("=-" * 20)
print("FIM DO CODIGO")