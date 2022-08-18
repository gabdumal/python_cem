print('-=-' * 14)
print(f'{"CONTAGEM DE VOGAIS":^42}')
print('-=-' * 14)
listagem = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for palavra in listagem:
    print(f'Na palavra {palavra.capitalize()} há as vogais', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f' {letra}', end='')
    print('')
