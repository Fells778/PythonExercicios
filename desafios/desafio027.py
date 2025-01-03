print("====== DESAFIO 27 ========")

nomeCompleto = str(input("Digite o seu nome completo: ")).strip()
nomeFatiado = nomeCompleto.split()
print("Prazer em te conhecer, {}.".format(nomeCompleto))
print("O seu primeiro nome é: {}.".format( nomeFatiado[0]))
print("O seu ultimo nome é: {}.".format(nomeFatiado[len(nomeFatiado) - 1]))

print("======== FIM DO CODIGO ========")