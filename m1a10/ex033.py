num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
numeros = [num1, num2, num3]
maiorNum = num1
menorNum = num1
for num in numeros:
    if num > maiorNum:
        maiorNum = num

    if num < menorNum:
        menorNum = num

print('O maior número é {}, e o menor número é {}.'.format(maiorNum, menorNum))