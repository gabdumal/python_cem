print('-=-' * 14)
print(f'{"LISTAGEM DE PREÇOS":^42}')
print('-=-' * 14)
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
for pos, item in enumerate(listagem):
    if pos % 2 == 0:
        print(f'{item:.<30}', end=' ')
    else:
        print(f'R${item:>7.2f}')
