distancia = int(input('Insira a distância da viagem em KM: '))
if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print('O valor da passagem é R$ {:.2f}'.format(valor))
