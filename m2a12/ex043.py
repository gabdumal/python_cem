print('-=-' * 6)
print('CÁLCULO DE IMC')
print('-=-' * 6)
peso = float(input('Digite seu peso em quilos: '))
altura = float(input('Digite sua altura em centímetros: ')) / 100

imc = peso / altura ** 2

print('IMC: {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida.')
