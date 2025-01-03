from time import sleep

print("========== DESAFIO 49 =========")
print('==== Tabela de mutiplicação ====')
num = int(input('Digite um número: '))
print('==== Tabuada ====')
print('-'*12)
for c in range(1, 11):
    multi = c * num
    print("{} x {} = {}".format(num, c, multi))
    sleep(0.3)
#   A forma mostrado na video aula foi essa:
#   num = int(input("Digite um número: "))
#   for c in range(1, 11):
#       print("{} x {} = {}".format(num, c, num * c))

print("-=" * 15)
print("FIM DO CODIGO")