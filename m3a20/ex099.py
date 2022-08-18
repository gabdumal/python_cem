from time import sleep

titulo = 'Descobre o maior'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)


# Funções
def maior(* num):
    print('Analisando os valores passados...')
    for c in num:
        print(c, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    valor_max = 0
    if len(num) != 0:
        valor_max = max(num)
    print(f'O maior valor informado foi {valor_max}.')
    print('-=-' * 10)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
