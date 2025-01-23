# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2,2)
# if 4 in num:
#     num.remove(5)
# else:
#     print("Não encontrei o número 5")
# num.remove(2)
# print(num)
# print(f"A lista tem {len(num)} elementos.")

# valores = []
# for cont in range(0,5):
#     valores.append(int(input("Digite um valor: ")))
#
# for c, v in enumerate(valores):
#     print(f"Na posição {c} tem o valor {v}...",)
# print("Fim da lista!")

a = [2,3,4,7]
b = a[:] # <- Cria uma copia
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")