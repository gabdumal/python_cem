cidade = str(input('Digite o nome da cidade: '))
if cidade.upper().startswith('SANTO'):
    print('A cidade {} começa com Santo'.format(cidade.capitalize()))
else:
    print('A cidade {} não começa com Santo'.format(cidade.capitalize()))
