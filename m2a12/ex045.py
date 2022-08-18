from random import randint
print('-=-' * 5)
print('JOKENPÔ')
print('-=-' * 5)
print('Vou jogar Jokenpô com você!\nSelecione sua jogada:\n [1] Pedra\n [2] Papel\n [3] Tesoura')
jogada = int(input('Jogada: '))

jogadaComp = randint(1, 3)
jogadaCompExt = ''

ganhador = ''

if jogada != 1 or jogada != 2 or jogada != 3:
    if jogadaComp == 1:
        if jogada == 1:
            ganhador = 'e'
        elif jogada == 2:
            ganhador = 'j'
        else:
            ganhador = 'c'
        jogadaCompExt = 'Pedra'
    elif jogadaComp == 2:
        if jogada == 1:
            ganhador = 'c'
        elif jogada == 2:
            ganhador = 'e'
        else:
            ganhador = 'j'
        jogadaCompExt = 'Papel'
    else:
        if jogada == 1:
            ganhador = 'j'
        elif jogada == 2:
            ganhador = 'c'
        else:
            ganhador = 'e'
        jogadaCompExt = 'Tesoura'
else:
    print('A opção selecionada é inválida.')

print('Minha jogada é {}!'.format(jogadaCompExt))
if ganhador == 'j':
    print('Parabéns! Você conseguiu ganhar de mim :(')
elif ganhador == 'c':
    print('EBA! Eu ganhei! Tente me vencer na próxima :D')
else:
    print('Empate :| Quem sabe na próxima alguém vença...')
