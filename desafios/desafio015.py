print("==== Desafio 15 ====")
dias = int(input("Quantos dias o carro foi alugado?: "))
kms = float(input("Informe quantos km foram percorridos?: "))
pago = (dias * 60) + (kms * 0.15)
print("O total a apagar é de R${:.2f}".format(pago))





