print('-=-' * 8)
print('ANALISADOR DE PRODUTOS')
print('-=-' * 8)
total = 0
quantidadeMaisMil = 0
precoMaisBarato = 0
prodMaisBarato = ''
while True:
    nome = input('Digite o nome do produto: ').strip()
    preco = float(input('Digite o preço do produto: R$'))
    if precoMaisBarato == 0:
        precoMaisBarato = preco
    total += preco
    if preco > 1000:
        quantidadeMaisMil += 1
    if preco <= precoMaisBarato:
        precoMaisBarato = preco
        prodMaisBarato = nome
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    print('-' * 20)
    if continuar == 'N':
        break
print(f'O total gasto na compra é R${total:.2f}')
print(f'{quantidadeMaisMil} produtos custam mais de R$1000.00.')
print(f'O nome do produto mais barato é {prodMaisBarato}')
