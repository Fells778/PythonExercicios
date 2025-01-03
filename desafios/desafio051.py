print("========== DESAFIO 51 =========")

primeiro = int(input("Priemiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end=" -> ")
print("FINAL")
print("-=" * 15)
print("FIM DO CODIGO")