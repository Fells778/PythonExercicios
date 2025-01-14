print("========== DESAFIO 70 =========")

print("=-" * 20)
print("==== LOJA SUPER BARATONA ===")
print("=-" * 20)
# Iniciando as variaveis com o valor 0
prodCaro = prodBarato = total = cont = 0
nomeProdBarato = ""
while True:
    nome = str(input("Informe o nome do produto: "))
    preco = float(input("Valor do produto: R$"))

    # Calcula quanto deu a compra...
    total += preco
    # Soma quantos produtos foram...
    cont += 1
    # Verifica quantos produtos com o valor maior que 1000...
    if preco > 1000:
        prodCaro += 1
    # Verifica o nome e o valor do produto mais barato...
    if cont == 1 or preco < prodBarato:
        prodBarato = preco
        nomeProdBarato = nome
    # Enquanto a pessoa não digitar sim ou não o codigo não continua...
    parar = " "
    while parar not in "SN":
        parar = str(input("Deseja continuar [S/N]:? ")).strip().upper()[0]
        print("=" * 25)
    # Se digitar não o codigo para...
    if parar in "Nn":
        break

# Aqui mostra as informações para o usuario...
print("=" * 30)
print(f"No total a compra deu: R${total:.2f}.")
print(f"Ao todo temos {prodCaro} custando mais de R$1000,00.")
print(f"E o prudto mais barato foi: {nomeProdBarato} e custa: {prodBarato}")

print("=-" * 30)
print("FIM DO CODIGO")
