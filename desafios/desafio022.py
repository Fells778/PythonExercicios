print("====== DESAFIO 22 ========")

nome = str(input("Digite o seu nome completo: ")).strip()

print("Analisando nome...")
print("...")
print("..")
print(".")
print("Transformando seu nome para letras maiúsculas: {}.".format(nome.upper()))
print("Transformando seu nome para letras minúsculas: {}.".format(nome.lower()))
print("Seu nome tem {} letras.".format(len(nome) - nome.count(" ")))
separar = nome.split()
print("O seu primeiro nome é {} e tem {} letras.".format(separar[0], len(separar[0])))

print("======== FIM DO CODIGO ========")