print('-=-' * 10)
print('CÁLCULO DE CATEGORIA')
print('-=-' * 10)

idade = int(input('Digite a idade do atleta: '))

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
