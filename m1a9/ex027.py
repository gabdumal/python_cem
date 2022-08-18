nome = str(input('Digite um nome: ')).strip()
print('NOME COMPLETO: {}\n Primeiro nome: {}\n Último nome: {}'. format(nome, nome.split()[0], nome.split()[-1]))
