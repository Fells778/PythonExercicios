print("========== DESAFIO 71 =========")

print("=-" * 20)
print("==== CAIXA ELETRONICO CEV ===")
print("=-" * 20)

valor = int(input("Digite o valor do saque: R$"))
total = valor
cedula = 100
totalCedula = 0

while True:
    # Verifica se pode tirar a cédula do valor digitado...
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        # Mosta a mesagem para o valor maior que 0...
        if totalCedula > 0:
            print(f"Total de {totalCedula} cédulas de R${cedula}.")
        # Verifica qual a cédula atual vai ser tirada...
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        # Volta o total de cédulas para 0 depois da verificação...
        totalCedula = 0
        # Verifica se o total chegou ao valor 0, se sim ele finaliza...
        if total == 0:
            break

print("=" * 30)
print("====== Saque finalizado ======")

print("=-" * 30)
print("FIM DO CODIGO")
