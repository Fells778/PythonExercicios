from datetime import date
print("========== DESAFIO 41 =========")

anoAtual = date.today().year
nascimento = int(input("Informe seu ano de nascimento: "))
idade = anoAtual - nascimento

if idade <= 9:
    print("Você que nasceu em {} tem {} anos. Categoria: MIRIM!".format(nascimento, idade))
elif 9 < idade <= 14:
    print("Você que nasceu em {} tem {} anos. Categoria: INFATIL!".format(nascimento, idade))
elif 14 < idade <= 19:
    print("Você que nasceu em {} tem {} anos. Categoria: JUNIOR!".format(nascimento, idade))
elif 19 < idade <= 25:
    print("Você que nasceu em {} tem {} anos. Categoria: SÊNIOR!".format(nascimento, idade))
else:
    print("Você que nasceu em {} tem {} anos. Categoria: MASTER!".format(nascimento, idade))

print("-=" * 15)
print("FIM DO CODIGO")