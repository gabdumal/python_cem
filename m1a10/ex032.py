ano = int(input('Digite o ano para saber se é bissexto: '))
print('O ano {} é bissexto.'.format(ano) if ano % 4 == 0 else 'O ano {} não é bissexto.'.format(ano))
