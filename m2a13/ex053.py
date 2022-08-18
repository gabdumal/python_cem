print('-=-' * 10)
print('DETECTOR DE PALÍNDROMOS')
print('-=-' * 10)
fraseOriginal = str(input('Digite uma frase: '))
frase = fraseOriginal.replace(' ', '')
fraseInversa = frase[::-1]
if frase.lower() == fraseInversa.lower():
    print('A frase \033[35m{}\033[m é um palíndromo!'.format(fraseOriginal))
else:
    print('A frase \033[35m{}\033[m não é um palíndromo!'.format(fraseOriginal))
