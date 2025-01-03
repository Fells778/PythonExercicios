from random import shuffle

print("===== Desafio 20 =====")

aluno1 = input("1° o nome do aluno: ")
aluno2 = input("2° o nome do aluno: ")
aluno3 = input("3° o nome do aluno: ")
aluno4 = input("4° o nome do aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("A ordem de apresentação é: ")
print(lista)

print("======= FIM DO CODIGO ========")