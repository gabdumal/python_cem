titulo = 'Matriz aprimorada'
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

somaPares = 0
somaTerceiraC = 0
maiorValorSegundaC = 0

for b, linha in enumerate(matriz):
    for c, num in enumerate(linha):
        print(f'[{num:^3}]', end='')
        if num % 2 == 0:
            somaPares += num
        if c == 1:
            if b == 0:
                maiorValorSegundaC = num
            if num > maiorValorSegundaC:
                maiorValorSegundaC = num
        if c == 2:
            somaTerceiraC += num
        if c in [2, 5]:
            print()

print('-=-' * numTituloDet)
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTerceiraC}.')
print(f'O maior valor da segunda coluna é {maiorValorSegundaC}.')
