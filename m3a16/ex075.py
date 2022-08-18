print('-=-' * 9)
print('ANÁLISE DE DADOS')
print('-=-' * 9)
num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
num3 = int(input('Digite o 3º valor: '))
num4 = int(input('Digite o 4º valor: '))
numeros = (num1, num2, num3, num4)
print(f'O valor 9 apareceu {numeros.count(9)} vez(es).')
if 3 in numeros:
    print(f'O primeiro valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado.')
pares = ''
print('O(s) número(s) par(es) digitado(s) foi(ram):', end='')
for num in numeros:
    if num % 2 == 0:
        print(f' {num}', end='')
