print('-=-' * 10)
print('SOMA DE VÁRIOS NÚMEROS')
print('-=-' * 10)
numero = 0
soma = 0
quantidade = 0
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 999:
        break
    soma += numero
    quantidade += 1
print(f'A soma de todos os números digitados é {soma}')
print(f'Foram digitados {quantidade} números.')

