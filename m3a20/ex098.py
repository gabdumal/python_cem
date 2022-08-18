from time import sleep

titulo = 'Contador'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)


# Funções
def contador(inicio_par, fim_par, passo_par):
    if inicio_par == fim_par or passo_par == 0:
        print('Você digitou valores inválidos.')
    else:
        print(f'Contagem de {inicio_par} até {fim_par} de {passo_par} em {passo_par}:')
        if inicio_par > fim_par:
            corretor = -1
            passo_par *= -1
        else:
            corretor = 1
        for c in range(inicio_par, fim_par + corretor, passo_par):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')


print('-=-' * 10)
contador(1, 10, 1)
print('---' * 10)
contador(10, 0, 2)
print('---' * 10)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('---' * 10)
contador(inicio, fim, passo)
