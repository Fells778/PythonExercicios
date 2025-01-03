from datetime import date

print("====== DESAFIO 032 =======")

ano = int(input("Digite o seu ano atual ou digite 0 (zero) para saber se o ano atual é bissexto ou não: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é bissexto!".format(ano))
else:
    print("O ano de {} não é bissexto!".format(ano))

print("Tenha um otimo ano!")

print("====== FIM DO CODIGO =========")
