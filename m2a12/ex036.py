print('-=-' * 12)
print('BANCO BOM BRASIL - Empréstimos')
print('-=-' * 12)
valorCasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Digite em quantos anos o empréstimo será quitado: '))

valorMensal = valorCasa / (anos * 12)

if valorMensal > salario * 0.3:
    print('Informamos que infelizmente o empréstimo foi negado.')
else:
    print('Seu empréstimo foi aprovado! O valor de pagamento mensal é R$ {:.2f}.'.format(valorMensal))
