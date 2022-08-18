print('-=-' * 5)
print('FATORIAL ')
print('-=-' * 5)
num = int(input('Digite o valor: '))
it = num
resultado = 1
while it > 0:
    resultado *= it
    it -= 1
print('O fatorial de {} é igual a {}.'.format(num, resultado))

