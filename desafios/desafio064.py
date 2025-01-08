print("========== DESAFIO 64 =========")

n = 0
cont = 0
soma = 0
# n = cont = soma = 0 //pode fazer assim tbm
n = int(input("Informe um número [Digite \033[4:30:42m999\033[m para parar]: "))
while n != 999:
    soma += n
    cont += 1
    n = int(input("Informe um número [Digite \033[4:30:42m999\033[m para parar]: "))

print("=-" * 20)
print("No total foram digitados {} números e a soma deles é {}.".format( cont, soma))
print("=-" * 20)
print("FIM DO CODIGO")