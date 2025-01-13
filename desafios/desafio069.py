print("========== DESAFIO 69 =========")

contIdade = homem = mulher = 0

while True:
    print("=-" * 20)
    print(" CADASTRANDO PESSOA ")
    print("=-" * 20)
    idade = int(input("Informe sua idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]

    parar = " "
    while parar not in "SN":
        parar = str(input("Deseja continuar [S/N]:? ")).strip().upper()[0]

    if idade >= 18:
        contIdade += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulher += 1

    if parar in "Nn":
        break

print("=" * 30)
print(f"No total temos {contIdade} pessoas com mais de 18 anos.")
print(f"Ao todo temos {homem} homens cadastrados.")
print(f"Temos {mulher} mulheres com menos de 20 anos")

print("=-" * 20)
print("FIM DO CODIGO")
