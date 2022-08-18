titulo = 'Texto adaptável'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)


# Funções
def escreva(msg):
    tamanhoMsg = len(msg) + 4
    print('~' * tamanhoMsg)
    print(f'  {msg}')
    print('~' * tamanhoMsg)


escreva('Olá mundo!')
