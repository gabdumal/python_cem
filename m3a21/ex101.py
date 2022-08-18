titulo = 'Permissão para votar'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)


# Funções
def voto(ano_nascimento_p):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento_p
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa principal
ano_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_nascimento))
