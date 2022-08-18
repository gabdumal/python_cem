i = 1
segmentos = []
print('-=-' * 10)
print('ANALISADOR DE TRIÂNGULOS 2.0')
print('-=-' * 10)
while i < 4:
    segmento = float(input('Digite o comprimento do {}º segmento em cm: '.format(i)))
    segmentos.append(segmento)
    i += 1

existe = True

if segmentos[0] + segmentos[1] < segmentos[2]:
    existe = False

if segmentos[1] + segmentos[2] < segmentos[0]:
    existe = False

if segmentos[0] + segmentos[2] < segmentos[1]:
    existe = False

if existe:
    print('O triângulo com os segmentos {}cm, {}cm e {}cm pode existir '.format(segmentos[0], segmentos[1], segmentos[2]), end='')
    if segmentos[0] == segmentos[1] == segmentos[2]:
        print('e é Equilátero.')
    elif segmentos[0] == segmentos[1] or segmentos[1] == segmentos[2] or segmentos[0] == segmentos[2]:
        print('e é Isósceles.')
    else:
        print('e é Escaleno.')

else:
    print('O triângulo com os segmentos {}cm, {}cm e {}cm não pode existir.'.format(segmentos[0], segmentos[1], segmentos[2]))
