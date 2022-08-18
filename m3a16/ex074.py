from random import randint
print('-=-' * 9)
print('NÚMEROS ALEATÓRIOS')
print('-=-' * 9)
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maiorValor = numeros[0]
menorValor = numeros[0]
for num in numeros:
    if num > maiorValor:
        maiorValor = num
    if num < menorValor:
        menorValor = num
print('A lista de números gerados é:', end='')
for num in numeros:
    print(f' {num}', end='')
print(f'\nO maior valor é {maiorValor} e o menor valor é {menorValor}.')