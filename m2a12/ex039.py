import datetime

print('-=-' * 12)
print('CÁLCULO DE TEMPO PARA ALISTAR-SE')
print('-=-' * 12)

anoNasc = int(input('Digite seu ano de nascimento: '))
anoAtual = datetime.datetime.now().year

idade = anoAtual - anoNasc

if idade < 18:
    print('Ainda falta(m) {} ano(s) para você ter que se alistar no exército.'.format(18 - idade))
elif idade > 18:
    print('Você está atrasado há {} ano(s) para se alistar no exército.'.format(idade - 18))
else:
    print('Você deve se alistar no exército neste ano.')


