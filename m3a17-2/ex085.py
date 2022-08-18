titulo = 'Lista com pares e ímpares'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

valores = [[], []]

for c in range(0, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1]. append(num)

print('-=-' * numTituloDet)

print(f'Os seguintes valores são pares: {sorted(valores[0])}.')
print(f'Os seguintes valores são ímpares: {sorted(valores[1])}.')
