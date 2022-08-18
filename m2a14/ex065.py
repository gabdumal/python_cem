print('-=-' * 10)
print('OPERAÇÕES DE VÁRIOS NÚMEROS')
print('-=-' * 10)
numero = 0
soma = 0
quantidade = 0
maior = 0
menor = 0
fim = 'N'
while fim == 'N':
    numero = int(input('Digite um número inteiro: '))
    fim = input('Deseja finalizar o programa? [S/N]').upper()
    if quantidade == 0:
        maior = numero
        menor = numero
    if fim not in 'SN':
        fim = 'N'
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero
    quantidade += 1
media = soma / quantidade
print('A média de todos os números digitados é {}'.format(media))
print('O maior valor entre os números digitados é {}'.format(maior))
print('O menor valor entre os números digitados é {}'.format(menor))

