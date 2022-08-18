velocidade = int(input('Insira a velocidade do veículo: '))
if velocidade > 80:
    print('O veículo foi multado por excesso de velocidade.\nValor da multa: R$ {:.2f}'.format((velocidade - 80)*7))
else:
    print('O veículo está dentro do limite de velocidade')
