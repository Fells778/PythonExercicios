print("========== DESAFIO 56 =========")

media = 0
somaidade = 0
maioridade = 0
totalmulher = 0
nomehomemvelho = ""
for c in range(1, 5):
    print("Pessoa n° {}".format(c))
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if c == 1 and sexo in "Mm":
        maioridade = idade
        nomehomemvelho = nome
    elif sexo in "Mm" and idade > maioridade:
        maioridade = idade
        nomehomemvelho = nome
    elif sexo in "Ff" and idade < 20:
        totalmulher += 1
    print("-" * 10)

media = somaidade / 4
print("A média de idade do grupo é de {} anos.".format(media))
print("O homem mais velho do grupo tem {} anos e se chama {}.".format(maioridade, nomehomemvelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totalmulher))
print("-=" * 15)
print("FIM DO CODIGO")
