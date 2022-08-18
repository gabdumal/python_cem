print('-=-' * 12)
print('CONVERSOR DE BASES NUMÉRICAS')
print('-=-' * 12)
numero = int(input('Digite um valor inteiro: '))
base = int(input('Selecione a base de conversão:\n 1 - Binário\n 2 - Octal\n 3 - Hexadecimal\n Base selecionada: '))

if base == 1:
    print('{} convertido para binário é {}.'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('{} convertido para octal é {}.'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é {}.'.format(numero, hex(numero)[2:].upper()))
else:
    print('A opção selecionada é inválida.')
