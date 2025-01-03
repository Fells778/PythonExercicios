print("========== DESAFIO 40 =========")

nota01 = float(input("Informe sua nota: "))
nota02 = float(input("Informe a segunda nota: "))

media = (nota01 + nota02) / 2
if media < 5:
    print("Média abaixo de 5: \033[4:31mREPROVADO\033[m")
    print("Sua média foi de \033[1:30:41{:.1f}\033m.".format(media))
elif 5 <= media < 6.9:
    print("Média entre 5 e 6.9: \033[4:33mRECUPERAÇÃO\033[m")
    print("Sua média foi de \033[1:30:43m{:.1f}\033[m.".format(media))
else:
    print("Média 7 ou superio: \033[4:32mAPROVADO\033[m")
    print("Sua média foi de \033[1:30:42m{:.1f}\033[m.".format(media))
print("-=" * 15)
print("FIM DO CODIGO")