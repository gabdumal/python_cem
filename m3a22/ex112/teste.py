from utilidadescev import moeda, dado

titulo = 'Operações com valores monetários formatados'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

b = dado.leia_dinheiro('Digite o preço: R$')
moeda.resumo(b, 80, 35)
