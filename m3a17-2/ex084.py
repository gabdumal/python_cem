titulo = 'lista composta e análise de dados'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

numPessoas = 0
maiorPeso = 0
menorPeso = 0
pessoasMaiorPeso = []
pessoasMenorPeso = []

while True:
    print(f'== Pessoa {numPessoas + 1} ==')
    nome = input('Nome: ')
    peso = float(input('Peso (Kg): '))
    if numPessoas == 0:
        maiorPeso = peso
        menorPeso = peso
    if peso > maiorPeso:
        maiorPeso = peso
        pessoasMaiorPeso.clear()
        pessoasMaiorPeso.append(nome)
    elif peso == maiorPeso:
        pessoasMaiorPeso.append(nome)
    if peso < menorPeso:
        menorPeso = peso
        pessoasMenorPeso.clear()
        pessoasMenorPeso.append(nome)
    elif peso == menorPeso:
        pessoasMenorPeso.append(nome)
    continuar = input('Deseja continuar? [S/N]').upper()
    if continuar == 'N':
        break
    numPessoas += 1

print('-=-' * numTituloDet)

print(f'Ao todo, você cadastrou {numPessoas + 1} pessoa(s).')
print(f'O maior peso foi de {maiorPeso}Kg, peso de {pessoasMaiorPeso}.')
print(f'O menor peso foi de {menorPeso}Kg, peso de {pessoasMenorPeso}.')
