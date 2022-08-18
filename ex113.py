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
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;33mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leia_float(msg):
    """
    -> Verifica se um valor é float.
    :param msg: A mensagem de input.
    :return: O valor verificado.
    """
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;33mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


# Programa principal
num_i = leia_int('Digite um número inteiro: ')
num_r = leia_float('Digite um número real: ')
print(f'O valor inteiro digitado foi {num_i} e o real foi {num_r}.')
