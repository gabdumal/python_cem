print('-=-' * 5)
print('CALCULADORA ')
print('-=-' * 5)
num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
fim = False
while not fim:
    print('= OPÇÕES =\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    operacao = int(input('Selecione a opção: '))
    if operacao == 1:
        print('Soma: ', num1 + num2)
    elif operacao == 2:
        print('Multiplicação: ', num1 * num2)
    elif operacao == 3:
        print('O maior é: ', max([num1, num2]))
    elif operacao == 4:
        num1 = int(input('Digite o 1º valor: '))
        num2 = int(input('Digite o 2º valor: '))
    elif operacao == 5:
        print('Encerrando o programa...')
        fim = True
    else:
        print('Opção inválida, selecione novamente...')
