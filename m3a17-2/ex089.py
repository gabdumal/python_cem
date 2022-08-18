titulo = 'Boletim'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

boletim = []

while True:
    nome = input('Nome: ').strip().capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    boletim.append([nome, n1, n2])
    continuar = input('Deseja continuar? [S/N]').upper()
    if continuar == 'N':
        break

print('-=-' * 9)
print('No. ', end='')
print(f'{"NOME":<16}', end='')
print(f'{"MÉDIA":<6}')
print('---' * 9)
for c, aluno in enumerate(boletim):
    print(f'{c:<4}', end='')
    print(f'{aluno[0]:<16}', end='')
    print(f'{(aluno[1] + aluno[2]) / 2:<6.2f}')
print('---' * 9)
while True:
    idAluno = int(input('Mostrar notas de qual aluno? (999 interrompe) No. '))
    if idAluno == 999:
        break
    elif idAluno < len(boletim):
        print(f'Notas de {boletim[idAluno][0]} são {boletim[idAluno][1]} e {boletim[idAluno][2]}.')
        print('---' * 9)
    else:
        print('Aluno não registrado, tente novamente...')
        print('---' * 9)
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
