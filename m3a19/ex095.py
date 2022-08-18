titulo = 'Cadastro de jogadores'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

listaJogadores = list()

while True:
    nome = input('Nome: ').strip().title()
    partidasJogadas = int(input('Nº de partidas jogadas: '))
    jogador = {'nome': nome, 'partidasJogadas': partidasJogadas}
    if partidasJogadas > 0:
        numGolsPorPartida = list()
        for c in range(0, partidasJogadas):
            numGols = int(input(f'Quantos gols na partida {c + 1}? '))
            numGolsPorPartida.append(numGols)
        jogador.update({'numGolsPorPartida': numGolsPorPartida})
    listaJogadores.append(jogador.copy())
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    else:
        print('-' * 30)

print('-=-' * 10)

print('cod ', end='')
print(f'{"NOME":<16}', end='')
print(f'{"GOLS":<20}', end='')
print(f'{"TOTAL":<2}')
print('---' * 16)
for c, jogador in enumerate(listaJogadores):
    print(f'{c:<4}', end='')
    print(f'{jogador["nome"]:<16}', end='')
    totalGols = 0
    if jogador['partidasJogadas'] > 0:
        print(f'{str(jogador["numGolsPorPartida"]):<20}', end='')
        for i, numGols in enumerate(jogador['numGolsPorPartida']):
            totalGols += numGols
    else:
        print(f'{"[0]":<20}', end='')
    print(f'{totalGols:<2}')
print('---' * 16)

while True:
    idJogador = int(input('Mostrar dados de qual jogador? (999 interrompe) No. '))
    if idJogador == 999:
        break
    elif 0 <= idJogador < len(listaJogadores):
        print(f'== LEVANTAMENTO DO JOGADOR {listaJogadores[idJogador]["nome"]}:')
        if listaJogadores[idJogador]['partidasJogadas'] > 0:
            for c in range(0, listaJogadores[idJogador]['partidasJogadas']):
                print(f'   No jogo {c + 1}, fez {listaJogadores[idJogador]["numGolsPorPartida"][c]} gols.')
        else:
            print('   Este jogador ainda não jogou em alguma partida.')
        print('---' * 20)
    else:
        print(f'ERRO! Não existe jogador com código {idJogador}, tente novamente...')
        print('---' * 20)
print('<< VOLTE SEMPRE >>')
