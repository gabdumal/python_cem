# num = str(input('Digite um número de 0 a 9999: '))
# num = num[-4:]
# num = num.zfill(4)
# print('Número {}\n Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(num, num[3], num[2], num[1], num[0]))
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
print('Número {}\n Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(num, u, d, c, um))
