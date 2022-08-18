frase = str(input('Escreva uma frase: ')).strip()
numVezesA = frase.upper().count('A')
if numVezesA > 0:
    print('FRASE: {}\n A letra A aparece {} vez(es)\n Primeira aparição da letra A: {}\n Última aparição da letra A: {}'.format(frase, numVezesA, frase.upper().find('A') + 1, frase.upper().rfind('A') + 1))
else:
    print('Não há letra A na frase {}'.format(frase))
