n = soma = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break #Para o codigo...
    soma += n
print("A soma vale {}.".format(soma))
print("FIM")
