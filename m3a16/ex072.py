print('-=-' * 8)
print('NÚMERO POR EXTENSO')
print('-=-' * 8)
numExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número: '))
    if 0 <= numero <= 20:
        print(f'O número {numero} por extenso é {numExtenso[numero].capitalize()}.')
        break
    else:
        print('Número inválido, tente novamente.')
