print('-=-' * 10)
print('MAIOR E MENOR PESOS')
print('-=-' * 10)
maiorPeso = 0
menorPeso = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso em Kg: '))
    if c == 0:
        maiorPeso = peso
        menorPeso = peso
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print('O maior peso é \033[35m{}\033[mKg, e o menor peso é \033[31m{}\033[mKg.'.format(maiorPeso, menorPeso))
