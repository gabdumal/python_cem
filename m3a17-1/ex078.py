titulo = 'Maior e menor da lista'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

valores = []

for c in range(0, 5):
    num = int(input('Digite um valor inteiro: '))
    valores.append(num)

print(f'Você digitou os valores {valores}.')
valorMax = max(valores)
numValorMax = valores.count(valorMax)
print(f'O maior valor da lista é {valorMax} e está na', end='')
if numValorMax > 1:
    print('s seguintes posições: ', end='')
    for c in range(0, numValorMax):
        print(f'{valores.index(valorMax, valores.index(valorMax) + c) + 1} ', end='')
    print()
else:
    print(f' {valores.index(valorMax) + 1}ª posição.')

valorMin = min(valores)
numValorMin = valores.count(valorMin)
print(f'O menor valor da lista é {valorMin} e está na', end='')
if numValorMin > 1:
    print('s seguintes posições: ', end='')
    for c in range(0, numValorMin):
        print(f'{valores.index(valorMin, valores.index(valorMin) + c) + 1} ', end='')
    print()
else:
    print(f' {valores.index(valorMin) + 1}ª posição.')
