salario = float(input('Digite o salário do funcionário: R$ '))
if salario > 1250:
    aumento = 10
    salarioNovo = salario * 1.1
else:
    aumento = 15
    salarioNovo = salario * 1.15

print('O salário R$ {:.2f} com o aumento de {}% é R$ {:.2f}.'.format(salario, aumento, salarioNovo))
