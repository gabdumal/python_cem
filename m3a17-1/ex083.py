titulo = 'Validando expressões matemáticas'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

pilha = []

expr = input('Digite uma expressão matemática: ')

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

print('-=-' * numTituloDet)

if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')

