print('-=-' * 10)
print('SEQUÊNCIA DE FIBONACCI')
print('-=-' * 10)
numero = int(input('Digite um número inteiro: '))
numTermos = int(input('Digite o número de termos a exibir: '))
i = 0
anterior = 0
while i < numTermos:
    print('{}'.format(numero), end='')
    numero += anterior
    anterior = numero - anterior
    if i != numTermos - 1:
        print(' -> ', end='')
    i += 1