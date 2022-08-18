from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
numAleatorio = randint(0, 5)
numero = int(input('Em que número eu pensei? '))
if numero == numAleatorio:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(numAleatorio, numero))
