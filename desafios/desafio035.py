print("====== DESAFIO 035 =======")

r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

print("=" * 20)
print("ANALISANDO...")
print("=" * 20)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos digitados PODEM formar um triângulo!")
else:
    print("Os segmentos digitados NÃO podem formar um triângulo!")
print("====== FIM DO CODIGO =========")