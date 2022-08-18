from time import sleep


# Funções
def borda(msg, bor='-=-', cor_pri='', cor_back=''):
    cor_pri = str(cor_pri)
    cor_back = str(cor_back)
    num_msg = len(msg) + 2
    num_msg_det = (num_msg // 3) + 1
    if cor_pri != '':
        cor_pri = cor_pri + '; '
    print(f'\033[{cor_pri}{cor_back}m{bor}\033[m' * num_msg_det)
    print(f'\033[{cor_pri}{cor_back}m{msg:^{num_msg_det * 3}}\033[m')
    print(f'\033[{cor_pri}{cor_back}m{bor}\033[m' * num_msg_det)


# Programa principal
borda('Sistema de ajuda PyHelp', cor_back=43)
while True:
    topico = input('Função ou biblioteca> ').strip()
    if topico == 'FIM':
        break
    topico = topico.lower()
    sleep(0.5)
    borda(f'Acessando o manual do comando \'{topico}\'', '~~~', cor_back=44)
    sleep(1)
    print('\033[30;47m')
    help(topico)
    print('\033[m', end='')
borda('Até logo!', cor_back=41)