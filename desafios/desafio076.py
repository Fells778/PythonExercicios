print("========== DESAFIO 76 =========")

prod = (
"Copo", 1.50, "Caenca", 4, "Mouse", 70, "Teclado", 85, "Monitor", 560, "Climatizador", 350, "Fone", 50, "Tenis", 50,
"Controle", 70)
total = 0
print("=" * 30)
print(f"{"Lista de preços":^30}")
print("=" * 30)
for item in range(0, len(prod)):
    if item % 2 == 0:
        print(f"{prod[item]:.<30}", end=" ")
    else:
        print(f"R$ {prod[item]:>5.2f}")
        total += prod[item]

print(f"Total:R$ {total}.")
print("=-" * 30)
print("FIM DO CODIGO")
