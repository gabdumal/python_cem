l = float(input('Digite a largura da parede em metros:'))
a = float(input('Digite a altura da parede em metros:'))
area = l*a
print('Informações sobre a parede\n Largura: {}m\n Altura: {}m\n Área: {}m²\n Tinta necessária: {}L'.format(l, a, area, area/2))