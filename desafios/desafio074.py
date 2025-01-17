from random import randint

print("========== DESAFIO 74 =========")

tuplaNumero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f"Os valores sorteados foram: ", end="")

for c in tuplaNumero:
    print(f"{c}", end=", ")

# Da para usar o max e o min no lugar de usar if e else para verificar
# qual é o maior valor e o menor valor...
print(f"\nO maior valor foi {max(tuplaNumero)} e o menor foi {min(tuplaNumero)}.")

print("=-" * 30)
print("FIM DO CODIGO")
