print("========== DESAFIO 42 =========")

r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos digitados PODEM formar um triângulo!")
    if r1 == r2 == r3:
        print("Todos os lados são iguais, triângulo: EQUILÁTERO")
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("Dois lados são iguais, triângulo: ISÓSCELES")
    else:
        print("Todos os lados são diferentes, triângulo: ESCALENO")
else:
    print("Os segmentos digitados NÃO podem formar um triângulo!")


print("-=" * 15)
print("FIM DO CODIGO")