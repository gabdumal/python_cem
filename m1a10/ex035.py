i = 1
retas = []
print('-=-' * 10)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 10)
while i < 4:
    reta = float(input('Digite o comprimento do {}º segmento em cm: '.format(i)))
    retas.append(reta)
    i += 1

existe = True

if retas[0] + retas[1] < retas[2]:
    existe = False

if retas[1] + retas[2] < retas[0]:
    existe = False

if retas[0] + retas[2] < retas[1]:
    existe = False

if existe:
    print('O triângulo com os segmentos {}cm, {}cm e {}cm pode existir.'.format(retas[0], retas[1], retas[2]))
else:
    print('O triângulo com os segmentos {}cm, {}cm e {}cm não pode existir.'.format(retas[0], retas[1], retas[2]))
