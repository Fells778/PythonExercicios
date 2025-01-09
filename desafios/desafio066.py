print("========== DESAFIO 65 =========")
cont = soma = 0

while True:
    n = int(input("Digite um número [digite 999 para parar]: "))
    if n == 999:
        break
    cont += 1
    soma += n

print("=-" * 20)
print(f"No total foram digitados {cont} números.")
print(f"E a soma deles é {soma}.")
print("Fim")
print("=-" * 20)
print("FIM DO CODIGO")
