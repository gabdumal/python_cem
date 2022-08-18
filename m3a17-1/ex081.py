titulo = 'Valores únicos em uma lista'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

valores = []

while True:
    num = int(input('Digite um número inteiro: '))
    valores.append(num)
    print('Valor adicionado com sucesso!')
    continuar = input('Deseja continuar? [S/N]').upper()
    if continuar == 'N':
        break

print('-=-' * numTituloDet)
print(f'Você digitou os valores {valores}.')
print(f'{len(valores)} números foram digitados.')
print(f'A lista de valores em ordem decrescente é {sorted(valores, reverse=True)}.')
print('O valor 5 ', end='')
if 5 not in valores:
    print('não ', end='')
print('foi digitado.')

