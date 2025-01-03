from datetime import date

print("========== DESAFIO 39 =========")

anoAtual = date.today().year
nascimento = int(input("Informe seu ano de nascimento: "))
idade = anoAtual - nascimento
print("Você que nasceu em {} tem {} anos em {}.".format(nascimento, idade, anoAtual))

if idade == 18:
    print("Alistamento obrigatorio!")
elif idade < 18:
    saldo = 18 - idade
    ano = anoAtual + saldo
    print("Você ainda não tem 18 anos, ainda falta {} anos para o seu alistamento".format(saldo))
    print("O seu ano de alistamento será em {}.".format(ano))
else:
    saldo = idade - 18
    ano = anoAtual - saldo
    print("Já deveria ter se alistado há {} anos!".format(saldo))
    print("O seu alistamento foi em {}.".format(ano))
print("-=" * 15)
print("FIM DO CODIGO")