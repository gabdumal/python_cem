km = float(input('Digite a quantidade de quilômetros percorridos: '))
dias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))
preco = 60 * dias + 0.15 * km
print('O valor do aluguel é R${:.2f}'.format(preco))
