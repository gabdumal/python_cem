titulo = 'Dividindo valores em várias listas'
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

pares = []
impares = []

for c in valores:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f'Você digitou os valores {valores}.')
print(f'Os seguintes valores são pares: {pares}.')
print(f'Os seguintes valores são ímpares: {impares}.')
