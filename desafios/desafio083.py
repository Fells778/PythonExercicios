print("========== DESAFIO 83 =========")

expr = str(input("Digite uma expressão: "))
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Sua expresão é válida")
else:
    print("Sua expressão não é válida")

print("=-" * 30)
print("FIM DO CODIGO")