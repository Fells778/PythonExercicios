print("Esse dessafio é pra mim mesmo")
print("========= CALCULADORA BASICA ========")
print("Esccolha a sua operação:")
print("[1] - Multplicação *")
print("[2] - Soma +")
print("[3] - Divisão /")
print("[4] - Subtração -")
print("-" * 30)
resultado = 0
escolha = int(input("Operação: "))
print("-" * 30)
for c in range(1, 2):
    num01 = float(input("Digite um valor: "))
    num02 = float(input("Degite mais um valor: "))
    if escolha == 1:
        resultado = num01 * num02
    elif escolha == 2:
        resultado = num01 + num02
    elif escolha == 3:
        if num01 > num02:
            resultado = num01 - num02
        elif num01 < num02:
            resultado = num02 - num01
print("A operação escolhida foi: {}".format(escolha))
print("É o resultado dessa operação é: {:.2f}".format(resultado))
print("-=" * 30)
print("================ FIM DO CODIGO ===============")
