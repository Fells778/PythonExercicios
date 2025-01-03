from random import randint
print("========== DESAFIO 58 =========")

print("Computador: Vou pensar em um número entre 0 e 10... Tente adivinhar qual foi!")
num_pc = randint(0, 10)
palpites = 1
num_usuario = int(input("Digite um número entre [0/10]: "))

while num_pc != num_usuario:
  palpites += 1
  print("Errou! Número escolhido pelo PC não foi esse")
  num_usuario = int(input("Tente novamente, digite um número: "))
  if num_pc > num_usuario:
      print("Está perto, tente de novo")
  elif num_pc < num_usuario:
      print("Quase, está no caminho")
print("=-" * 20)
print("Parabéns, você acertou! Com um total de {} tentativas.".format(palpites))
print("Computador escolheu {} e jogador o número {}.".format(num_pc, num_usuario))


print("=-" * 20)
print("FIM DO CODIGO")