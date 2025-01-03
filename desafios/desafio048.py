print("========== DESAFIO 48 =========")

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 ==0:
        cont = cont + 1 #ou cont += 1
        soma = soma + c #ou soma += c
print("A soma de todos os {} valores é igual a: {}.".format(cont ,soma))

# for c in range (2, 501, 2):
#     if c % 2 == 0:
#         cont += 1
#         soma += c
# print("A soma de todos os {} valores é igual a: {}.".format(cont, soma))

print("-=" * 15)
print("FIM DO CODIGO")