from random import randint
from time import sleep

titulo = 'Mega Sena'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

numJogos = int(input('Quantos jogos você quer que eu sorteie? '))

listaJogos = []

for c in range(0, numJogos):
    jogo = []
    i = 0
    while i < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            i += 1
    listaJogos.append(jogo[:])

print(f'-=-=-= SORTEANDO {numJogos} JOGOS =-=-=-')
for c, jogo in enumerate(listaJogos):
    sleep(1)
    print(f'Jogo {c + 1}: {sorted(jogo)}')
print(f'-=-=-=-= < BOA SORTE > =-=-=-=-')
