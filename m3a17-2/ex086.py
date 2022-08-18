titulo = 'Matriz'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 9):
    num = int(input('Digite um número inteiro: '))
    if c < 3:
        matriz[0][c] = num
    elif c < 6:
        matriz[1][c - 3] = num
    else:
        matriz[2][c - 6] = num

print('-=-' * numTituloDet)

for linha in matriz:
    for c, num in enumerate(linha):
        print(f'[{num:^3}]', end='')
        if c in [2, 5]:
            print()
