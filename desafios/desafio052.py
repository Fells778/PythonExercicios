print("========== DESAFIO 52 =========")

num = int(input("Digite um número: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[4:32m", end="")
        total += 1
    else:
        print("\033[033m", end="")
    print("{}".format(c), end=" | ")
print("O núemro {} foi dividido {}x".format(num, total))
if total == 2:
    print("Por isso ele é primo!")
else:
    print("Ele não é primo!")
print("-=" * 15)
print("FIM DO CODIGO")
