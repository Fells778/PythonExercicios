from math import  radians, sin, cos, tan

print("===== Desafio 18 =====")

angulo = float(input("Digite o valor do ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("O ângulo de {}° tem o Seno de {:.2f}.".format(angulo, seno))
print("O ângulo de {}° tem o Cosseno de {:.2f}.".format(angulo, cosseno))
print("O ângulo de {}° tem a tangente de {:.2f}.".format(angulo, tangente))

print("====== FIM DO CODIGO =======")