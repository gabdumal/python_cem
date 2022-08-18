print('-=-' * 3)
print('TABUADA')
print('-=-' * 3)
numero = int(input('Digite um número para calcular sua tabuada: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(numero, c, numero * c))
