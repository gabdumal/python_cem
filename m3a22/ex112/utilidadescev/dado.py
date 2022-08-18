def leia_dinheiro(msg):
    while True:
        v = str(input(msg))
        v = v.replace(',', '.').strip()
        if v.isalpha() or v == '':
            print(f'\033[0;31mERRO! \"{v}\" é um preço inválido.\033[m')
        else:
            return float(v)
