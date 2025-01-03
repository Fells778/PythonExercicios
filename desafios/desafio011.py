print('==== Quanto de tinta vai ser nescessária para pintar a parede? ====')
altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largaura da parede: '))
area = altura * largura
tinta = area / 2

print('Com uma área de {}m vão ser nescessarios {}L de tinta.'.format(area, tinta))

print('=== FIM DO CÓDIGO ===')