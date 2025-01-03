n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoInteira = n1 // n2
potencia = n1 ** n2
restoDivisao = n1 % n2

print('A soma é {},\n o produto é {} e a divisão é {:.3f}'.format(soma, multiplicacao, divisao))
print(
    'A divisão inteira é {} o resto da divisão é {} e a pontencia vale {}'.format(divisaoInteira,restoDivisao, potencia))
