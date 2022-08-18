import moeda

titulo = 'Operações com valores monetários formatados'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

b = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(b)} é {moeda.metade(b, True)}.')
print(f'O dobro de {moeda.moeda(b)} é {moeda.dobro(b, True)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(b, 10, True)}.')
print(f'Reduzindo 13%, temos {moeda.diminuir(b, 13, True)}.')
