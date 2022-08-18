titulo = 'Valores únicos em uma lista'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

valores = []

while True:
    num = int(input('Digite um número inteiro: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não foi adicionado à lista.')
    continuar = input('Deseja continuar? [S/N]').upper()
    if continuar == 'N':
        break
print('-=-' * numTituloDet)
print(f'Você digitou os valores {sorted(valores)}.')
