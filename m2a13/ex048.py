print('-=-' * 25)
print('SOMA DE TODOS OS NÚMEROS ÍMPARES MÚLTIPLOS DE TRÊS ENTRE 1 E 500')
print('-=-' * 25)
soma = 0
for c in range(1, 501):
    if (c % 3) == 0 and (c % 2) != 0:
        soma += c
print(soma)
