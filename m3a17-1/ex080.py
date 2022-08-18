titulo = 'Lista ordenada sem repetições'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

valores = []

for c in range(0, 5):
    num = int(input('Digite um número inteiro: '))
    if c == 0:
        valores.append(num)
    else:
        for i in range(len(valores), -1, -1):
            if i == 0:
                valores.insert(i, num)
            if num > valores[i - 1]:
                valores.insert(i, num)
                break

print('-=-' * numTituloDet)
print(f'Você digitou os valores {valores}.')
