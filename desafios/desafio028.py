from random import randint
from time import sleep
print("===== DESAFIO 28 =====")
print("-=-" * 27)
print("Computador: Vou pensar em um número entre 0 e 5... Tente adivinhar qual foi!")
print("-=-" * 27)
num_pc = randint(0, 5)
num_usuario = int(input("Digite um número entre 0 e 5: "))
print("Analisando...")
sleep(1)
print("=" * 20)
if num_pc == num_usuario:
    print("O seu número foi: {}.\ne o do computador foi: {}".format(num_usuario, num_pc))
    print("Parabéns você escolheu o mesmo número do computador!")
else:
    print("Poxa, você escolheu {} e o computador {}.".format(num_usuario, num_pc))
print("====== Obrigado por jogar! ======")
print("====== FIM DO CODIGO =========")