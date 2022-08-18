titulo = 'Ficha do jogador'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)


# Funções
def ficha(nome='<desconhecido>', gols=0):
    """
    -> Exibe a ficha de um jogador.
    :param nome: (opcional) O nome do jogador.
    :param gols:(opcional) Número de gols que o jogador fez.
    :return: Sem retorno.
    """
    print(f'O jogador {nome} fez {gols} gol(s).')


# Programa principal
n = input('Nome do jogador: ').strip().title()
g = input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
help(ficha)
