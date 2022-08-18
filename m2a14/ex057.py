print('-=-' * 10)
print('LEITOR DE SEXO')
print('-=-' * 10)
sexo = ''
sexo = input('Digite seu sexo (F ou M): ').strip().upper()
while sexo not in 'FM':
    print('Sexo inválido, digite novamente.')
    sexo = input('Digite seu sexo (F ou M): ').upper()
print('Sexo registrado com sucesso')
