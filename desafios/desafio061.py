print("========== DESAFIO 61 =========")

print("Gerando PA...")
print("=-" * 20)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end="")
    termo += razao
    cont += 1
print("FIM!")
print("=-" * 20)
print("FIM DO CODIGO")
