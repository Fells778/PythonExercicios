print("========== DESAFIO 37 =========")

num = int(input("Digite um número inteiro: "))
print("====== BASE DE CONVERSÃO ======")
print("[1] converte para BINÁRIO")
print("[2] converte para OCTAL")
print("[3] converte para HEXADECIMAL")

escolha = int(input("Escolha: "))
if escolha == 1:
    print("{} convertido para BINÁRIO é igual a {}.".format(num, bin(num) [2:]))
elif  escolha == 2:
    print("{} convertido para OCTAL é igual a {}.".format(num, oct(num) [2:]))
elif escolha == 3:
    print("{} convertido para HEXADECIMAL é igual a {}.".format(num, hex(num) [2:]))
else:
    print("Digite uma das opções validas!")
print("-=" * 15)
print("FIM DO CODIGO")