print("========== DESAFIO 75 =========")

n = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")),
     int(input("Digite um número: ")))

print("=" * 30)
print(f"Números digitados: {n}")
print(f"O número 9 apareceu {n.count(9)} vezes.")
if 3 in n:
     print(f"O número 3 está na {n.index(3)+1}°")
else:
     print("O número 3 não foi digitado")
print("Os núemros pares foram: ", end="")
for c in n:
     if c % 2 == 0:
          print(c, end="\n")

print("=-" * 30)
print("FIM DO CODIGO")
