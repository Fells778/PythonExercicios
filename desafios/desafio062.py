print("========== DESAFIO 62 =========")

print("Gerando PA...")
print("=-" * 20)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end="")
        termo += razao
        cont += 1
    print("PAUSA!")
    mais = int(input("Quantos termos você quer mostrar a mais?: "))
print("=-" * 20)
print("FIM!")
print("Progresão finalizada com {} termos mostrados".format(total))
print("=-" * 20)
print("FIM DO CODIGO")