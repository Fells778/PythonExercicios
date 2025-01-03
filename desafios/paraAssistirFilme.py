import random
import time

print("-=" * 20)
print("====== Escolha de Filmes =======")
print("-=" * 20)
filme01 = input("Nome do filme: ")
filme02 = input("Nome do outro filme: ")
lista = [filme01, filme02]
escolha = random.choice(lista)
print("-=" * 20)
print("Analisando...")
time.sleep(2)
print(f"O filme escolhido foi: {escolha}.")
print("-=" * 20)
print("FIM DO CODIGO!")
