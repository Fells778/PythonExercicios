nome = str(input("Qual é o seu nome?: "))

if nome == "Felipe":
    print("Que nome lindo!")
elif nome == "Pedro" or  nome == "Ana" or nome == "Maria":
    print("Seu nome é bem popular no Brasil.")
else:
    print("Que nome legal!")
print("Tenha um otimo dia, {}!".format(nome))