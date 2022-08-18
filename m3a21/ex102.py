titulo = 'Fatorial opcional'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)


# Funções
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show:(opcional) Mostrar ou não a conta.
    :return: O valor do fatorial calculado.
    """
    resultado = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        resultado *= c
    return resultado


# Programa principal
numero = int(input('Qual número deseja calcular? '))
mostrar = input('Deseja exibir o processo de cálculo? [S/N] ').strip().upper()
if mostrar == 'S':
    print(fatorial(numero, show=True))
else:
    print(fatorial(numero))
help(fatorial)
