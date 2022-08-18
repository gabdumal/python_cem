from random import sample
n1 = str(input('Digite o nome do 1º aluno: '))
n2 = str(input('Digite o nome do 2º aluno: '))
n3 = str(input('Digite o nome do 3º aluno: '))
n4 = str(input('Digite o nome do 4º aluno: '))
lista = [n1, n2, n3, n4]
lista2 = list(sample(lista, 4))
print('A ordem de apresentação é ')
print(lista2)
