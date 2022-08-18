print('-=-' * 7)
print('É NÚMERO PRIMO?')
print('-=-' * 7)
numero = int(input('Digite um número inteiro: '))
totalDivisiveis = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        totalDivisiveis += 1
        print('\033[36m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes, '.format(numero, totalDivisiveis), end='')

if totalDivisiveis > 2:
    print('logo, ele não é primo.'.format(numero))
else:
    print('logo, ele é primo.'.format(numero))
