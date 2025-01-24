print("========== DESAFIO 78 =========")

n = []
v = ""
for c in range(0,5):
    n.append(int(input("Digite um valor: ")))

print("=-" * 30)
print(F"Você digitou os valores: {n}")
print(f"O maior valor foi {max(n)} na posição: ", end="")
for i, p in enumerate(n):
    if p == max(n):
        print(f"{i}...", end="")
print("")
print(f"O menor valor foi: {min(n)} na posição: ", end="")
for i, p in enumerate(n):
    if p == min(n):
        print(f"{i}...", end="")
print("")
print("=-" * 30)
print("FIM DO CODIGO")