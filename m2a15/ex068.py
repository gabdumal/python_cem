from random import randint
print('-=-' * 5)
print('PAR OU ÍMPAR')
print('-=-' * 5)
print('Vou jogar Par ou Ímpar com você!')
rodadas = 0
while True:
    jogTipo = input('Você é ímpar ou par? [I/P] ').strip().upper()
    if jogTipo in 'IP':
        if jogTipo == 'I':
            print('Está bem, sou Par!')
        else:
            print('Está bem, sou ímpar!')
        jogNum = int(input('Qual é a sua jogada de 0 a 10? '))
        if 0 <= jogNum <= 10:
            jogNumComp = randint(0, 10)
            print(f'Eu jogo {jogNumComp}!')
            soma = jogNum + jogNumComp
            print(f'A soma deu {soma}!')
            if soma % 2 == 0:
                if jogTipo == 'P':
                    print('Parabéns! Você venceu essa rodada. Prepare-se para a próxima...')
                    rodadas += 1
                else:
                    print(f'EBA, eu ganhei! Você havia ganhado {rodadas} rodada(s).')
                    break
            else:
                if jogTipo == 'I':
                    print('Parabéns! Você venceu essa rodada. Prepare-se para a próxima...')
                    rodadas += 1
                else:
                    print(f'EBA, eu ganhei! Você havia ganhado {rodadas} rodada(s).')
                    break
        else:
            print('Jogada inválida, tente novamente...')
    else:
        print('Jogada inválida, tente novamente...')
