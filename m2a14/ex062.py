print('-=-' * 10)
print('PROGRESSÃO ARITMÉTICA')
print('-=-' * 10)
numero = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
i = 1
maisTermos = 11
while i < maisTermos:
    print('{}º termo: {}'.format(i, numero))
    numero += razao
    if i == maisTermos - 1:
        maisTermos += int(input('Quantos termos você deseja exibir? '))
    i += 1

print('Encerrando o programa...')
