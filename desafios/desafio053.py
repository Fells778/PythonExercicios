print("========== DESAFIO 53 =========")

frase = str(input("Digite uma frasea:")).strip().upper()
palavras = frase.split()
juntar = "".join(palavras)
inverso = ""
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
if inverso == juntar:
    print("Essa frase é um palíndromo!")
else:
    print("A frase digitada não é um palídromo!")
print("Você digitou: {}".format(juntar))
print("Ao contrario fica: {}.".format(inverso))

print("-=" * 15)
print("FIM DO CODIGO")