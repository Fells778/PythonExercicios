from math import trunc
print("==== Desafio 16 ====")
num = float(input("Digite um número: "))
# Sem importar, apenas usando o Int
print("O número {} tem a parte inteira {}.".format(num, int(num)))

# Ou
# Importando o trunc
print("O número {} tem a parte inteira {}.".format(num, trunc(num)))
print("=========== FIM DO PROGRAMA ==========")
