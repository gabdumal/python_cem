print('-=-' * 10)
print('SOMA DE VÁRIOS NÚMEROS')
print('-=-' * 10)
numero = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número inteiro: '))
    soma += numero
soma -= 999
print('A soma de todos os números digitados é {}'.format(soma))
