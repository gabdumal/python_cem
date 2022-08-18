titulo = 'Controle de terrenos'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)


# Funções
def area(lar, com):
    a = largura * comprimento
    print(f'A área de um terreno de {lar}m x {com}m é de {a:.2f}m².')


largura = float(input('Largura (m²): '))
comprimento = float(input('Comprimento (m²): '))
area(largura, comprimento)
