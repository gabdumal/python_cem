print('-=-' * 10)
print('CÁLCULO DE APROVAÇÃO')
print('-=-' * 10)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
