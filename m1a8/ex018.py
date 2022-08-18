import math
a = float(input('Digite um ângulo: '))
print('Ângulo {}°\n Seno: {:.2f}\n Cosseno: {:.2f}\n Tangente: {:.2f}'.format(a, math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))
