import datetime
print('-=-' * 10)
print('QUANTOS SÃO MAIORES?')
print('-=-' * 10)
anoAtual = datetime.datetime.now().year
numMaiores = 0
for c in range(0, 7):
    anoNasc = int(input('Digite seu ano de nascimento: '))
    if anoAtual - anoNasc >= 18:
        numMaiores += 1
print('\033[35m{}\033[m pessoas são maiores de idade, e \033[31m{}\033[m são menores de idade.'.format(numMaiores, 7 - numMaiores))
