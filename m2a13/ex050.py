print('-=-' * 7)
print('SOMAS DOS PARES')
print('-=-' * 7)
soma = 0
for c in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
print('O resultado da soma de todos os números pares é {}.'.format(soma))
