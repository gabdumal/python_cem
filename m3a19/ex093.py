titulo = 'Cadastro de jogador'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

jogador = dict()

print('Insira os dados do jogador')
nome = input('Nome: ').strip().title()
partidasJogadas = int(input('Nº de partidas jogadas: '))
jogador = {'nome': nome, 'partidasJogadas': partidasJogadas}
if partidasJogadas > 0 :
    numGolsPorPartida = list()
    for c in range(0, partidasJogadas):
        numGols = int(input(f'Quantos gols na partida {c + 1}? '))
        numGolsPorPartida.append(numGols)
    jogador.update({'numGolsPorPartida': numGolsPorPartida})

print('-=-' * 10)
print('Dados do jogador:')
for k, v in jogador.items():
    print(f'{k.capitalize()} tem valor {v}.')
print('-=-' * 10)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidasJogadas"]} partida(s).')
totalGols = 0
if jogador['partidasJogadas'] > 0:
    for i, c in enumerate(jogador['numGolsPorPartida']):
        print(f'    => Na partida {i + 1}, fez {c} gols.')
        totalGols += c
print(f'Foi um total de {totalGols} gol(s).')
