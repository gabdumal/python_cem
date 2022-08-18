from random import randint
from time import sleep

titulo = 'Sortear e somar'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)


# Funções
def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        rand_num = randint(0, 10)
        sleep(0.5)
        print(rand_num, end=' ')
        numeros.append(rand_num)
    print('PRONTO!')


def soma_par(numeros_par):
    soma = 0
    for num in numeros_par:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {numeros_par}, temos {soma}.')


# Variáveis
numeros = list()
sorteia()
soma_par(numeros)