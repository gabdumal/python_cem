def aumentar(v, a, f=False):
    r = v * (1 + (a / 100))
    if f:
        return moeda(r)
    else:
        return r


def diminuir(v, d, f=False):
    r = v - (v * (d / 100))
    if f:
        return moeda(r)
    else:
        return r


def metade(v, f=False):
    r = v / 2
    if f:
        return moeda(r)
    else:
        return r


def dobro(v, f=False):
    r = v * 2
    if f:
        return moeda(r)
    else:
        return r


def moeda(msg):
    return f'R${msg:.2f}'


def resumo(v, a, d):
    print('—' * 29)
    print('      RESUMO DO VALOR      ')
    print('—' * 29)
    print(f'{"Preço analisado:":<19}{moeda(v):>10}')
    print(f'{"Dobro do preço:":<19}{dobro(v, True):>10}')
    print(f'{"Metade do preço:":<19}{metade(v, True):>10}')
    print(f'{str(a) + "% de aumento:":<19}{aumentar(v, a, True):>10}')
    print(f'{str(d) + "% de redução:":<19}{diminuir(v, d, True):>10}')
    print('—' * 29)


