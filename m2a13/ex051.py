print('-=-' * 10)
print('PROGRESSÃO ARITMÉTICA')
print('-=-' * 10)
numero = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
i = 1
for c in range(0, 10):
    print('{}º termo: {}'.format(i, numero))
    numero += razao
    i += 1
