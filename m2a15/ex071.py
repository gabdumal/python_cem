print('-=-' * 8)
print('CAIXA ELETRÔNICO')
print('-=-' * 8)
saque = int(input('Digite o valor a ser sacado: R$'))
resto = saque
n50 = resto // 50
resto = resto % 50
n20 = resto // 20
resto = resto % 20
n10 = resto // 10
resto = resto % 10
n1 = resto
print(f'O saque será emitido nas seguintes quantidades:')
if n50 > 0:
    print(f'{n50} cédula(s) de R$50.00')
if n20 > 0:
    print(f'{n20} cédula(s) de R$20.00')
if n10 > 0:
    print(f'{n10} cédula(s) de R$10.00')
if n1 > 0:
    print(f'{n1} cédula(s) de R$1.00')
