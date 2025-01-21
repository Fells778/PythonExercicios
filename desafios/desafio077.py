print("========== DESAFIO 77 =========")

tupla = ("PROGRAMAR", "APRENDER", "PYTHON", "EMPREGO", "CURSO")

for c in tupla:
    print(f"Palavra: {c.upper()} vogal: ", end="")
    for letra in c:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
    print("")
print("=-" * 30)
print("FIM DO CODIGO")