print('-=-' * 5)
print('TABUADA 3.0')
print('-=-' * 5)
while True:
    numero = int(input('Digite um número para calcular sua tabuada: '))
    if numero < 0:
        break
    for c in range(0, 11):
        print('{} x {} = {}'.format(numero, c, numero * c))
    print('-' * 20)

