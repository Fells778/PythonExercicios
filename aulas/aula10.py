# nome = str(input("Dgite o seu nome: "))
# if nome == "Felipe":
#     print("Que nome mais lindo!")
# else:
#     print("Que nome bacana!")
# print("Bom dia, {}!".format(nome))

n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
media = (n1 + n2) / 2
print("A sua media foi de {:.1f}".format(media))
if media >= 6.0:
    print("Parabéns, sua media foi boa!")
else:
    print("Sua media poderia ter sido melhor, mas não desanime, estude mais!")
print("======== FIM ========")