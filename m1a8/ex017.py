from math import hypot
co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
print('A hipotenusa do triângulo retângulo cujos catetos medem {} e {} é igual a {:.3f}'.format(co, ca, hypot(co, ca)))
