import datetime

titulo = 'Cadastro de trabalhador'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

trabalhador = dict()

print('Insira os dados do trabalhador')
nome = input('Nome: ').strip().title()
anoNasc = int(input('Ano de nascimento: '))
carteira = int(input('Nº da carteira de trabalho (0 se não tiver): '))
anoAtual = datetime.datetime.now().year
idade = anoAtual - anoNasc
trabalhador = {'nome': nome, 'idade': idade}
if carteira != 0:
    anoCont = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$ '))
    aposentadoria = idade + anoCont + 35 - anoAtual
    trabalhador.update({'carteira': carteira, 'tempo para aposentadoria': aposentadoria, 'salário': salario})

print('-=-' * 10)

print('Dados do trabalhador:')

for k, v in trabalhador.items():
    print(f'{k.capitalize()} tem valor {v}.')
