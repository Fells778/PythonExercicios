print("========== DESAFIO 72 =========")


tupla = (
"zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
"quatorze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove", "vinte")

while True:

    n = int(input("Digite um núemro entre 0 e 20: "))
    if 0 <= n <= 20:
        break
    print("Tente novamente com um número entre 0 e 20")

print(f"Você digitou o número {tupla[n]}")

print("=-" * 30)
print("FIM DO CODIGO")