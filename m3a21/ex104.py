titulo = 'Verifica se é inteiro'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)


# Funções
def leia_int(msg):
    """
    -> Verifica se um valor é inteiro.
    :param msg: A mensagem de input.
    :return: O valor verificado.
    """
    while True:
        valor = str(input(msg)).strip()
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


# Programa principal
n = leia_int('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')
