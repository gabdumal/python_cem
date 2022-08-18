print('-=-' * 10)
print('DADOS DE PESSOAS')
print('-=-' * 10)
somaIdades = 0
maiorIdadeHomem = 0
nomeHomemMaisVelho = ''
numMulheresMenos20 = 0
for c in range(0, 4):
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (F ou M): ').upper()
    print('')
    somaIdades += idade
    if sexo == 'M':
        if idade > maiorIdadeHomem:
            maiorIdadeHomem = idade
            nomeHomemMaisVelho = nome
    else:
        if idade < 20:
            numMulheresMenos20 += 1
mediaIdades = somaIdades / 4
print('A média de idade do grupo é \033[35m{}\033[m anos.'.format(mediaIdades))
print('O nome do homem mais velho é \033[35m{}\033[m.'.format(nomeHomemMaisVelho))
print('\033[35m{}\033[m mulher(es) têm menos de 20 anos.'.format(numMulheresMenos20))
