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
