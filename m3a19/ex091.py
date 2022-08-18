from random import randint
from time import sleep

titulo = 'Jogo de dados'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

jogadas = list()

print('Os valores sorteados foram:')
for c in range(0, 4):
    num = randint(1, 6)
    print(f'{num} para o Jogador {c + 1}.')
    jogada = {'jogador': c + 1, 'numero': num}
    jogadas.append(jogada.copy())

print('-=-' * 10)

listaJogadasOrdenada = sorted(jogadas, key=lambda k: k['numero'], reverse=True)
print('Ranking dos Jogadores')
for i, jogada in enumerate(listaJogadasOrdenada):
    sleep(1)
    print(f'{i + 1}º lugar: Jogador {jogada["jogador"]}, com {jogada["numero"]} ponto(s).')
