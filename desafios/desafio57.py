print("========== DESAFIO 57 =========")

sexo = str(input("Digite seu sexo [M ou F]: ")).strip().upper()[0]

while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print("-=" * 20)
print("Sexo {} registrado com sucesso!".format(sexo))


print("FIM DO CODIGO")