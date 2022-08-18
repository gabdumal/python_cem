from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar... ')
print('-=-' * 20)
numAleatorio = randint(0, 10)
numTentativas = 1
numero = int(input('Em que número eu pensei? '))
fim = False
while not fim:
    if numero == numAleatorio:
        print('PARABÉNS! Você conseguiu me vencer em {} tentativa(s)!'.format(numTentativas))
        fim = True
    else:
        print('GANHEI! Eu pensei no número {} e não no {}. Tente pela {}ª vez.'.format(numAleatorio, numero, numTentativas + 1))
        numTentativas += 1
        numAleatorio = randint(0, 10)
        numero = int(input('Em que número eu pensei? '))

