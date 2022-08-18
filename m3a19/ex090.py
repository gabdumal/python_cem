titulo = 'Dicionário'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

aluno = dict()

print('Preencha os dados do aluno')
nome = input('Nome: ').strip().capitalize()
media = float(input('Média: '))
if media >= 6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
aluno = {'nome': nome, 'media': media, 'situacao': situacao}

print('-=-' * 10)

print('')
