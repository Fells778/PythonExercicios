print("====== DESAFIO 22 ========")

num = int(input("Digite um número: "))
num_convertido = str(num)
unidae = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print("Analisando o número {}...".format(num_convertido))
print("Unidade: {}.".format(unidae))
print("Dezena: {}.".format(dezena))
print("Centena: {}.".format(centena))
print("Milhar: {}.".format(milhar))

print("======== FIM DO CODIGO ========")