titulo = 'Cadastro de pessoas'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)

listaPessoas = list()

while True:
    pessoa = dict()
    print('Insira os dados da pessoa')
    nome = input('Nome: ').strip().title()
    sexo = input('Sexo: [F/M] ').strip().upper()
    idade = int(input('Idade: '))
    if sexo in 'MF':
        pessoa = {'nome': nome, 'sexo': sexo, 'idade': idade}
        listaPessoas.append(pessoa.copy())
        print('Pessoa cadastrada com sucesso!')
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        if continuar == 'N':
            break
    else:
        print('Valores digitados inválidos. Tente novamente...')

print('-=-' * 10)
print(f'— O grupo tem {len(listaPessoas)} pessoas.')
somaIdades = 0
listaMulheres = list()
for pessoa in listaPessoas:
    somaIdades += pessoa['idade']
    if pessoa['sexo'] == 'F':
        listaMulheres.append(pessoa['nome'])
mediaIdades = somaIdades / len(listaPessoas)
print(f'— A média de idade é de {mediaIdades:.2f} anos.')
listaAcimaMedia = list()
for pessoa in listaPessoas:
    if pessoa['idade'] > mediaIdades:
        listaAcimaMedia.append(pessoa)
print('— Lista das pessoas que estão acima da média de idade:')
for pessoa in listaAcimaMedia:
    for k, v in pessoa.items():
        print(f'{k} = {v}; ', end='')
    print()
print('<< ENCERRADO >>')
