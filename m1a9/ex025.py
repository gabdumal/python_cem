nome = str(input('Digite um nome: ')).strip()
listaNome = nome.upper().split()
if 'SILVA' in listaNome:
    print('O nome {} contém Silva'.format(nome))
else:
    print('O nome {} não contém Silva'.format(nome))
