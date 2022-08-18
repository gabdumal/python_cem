print('-=-' * 7)
print('CADASTRO DE PESSOAS')
print('-=-' * 7)
pessoasMais18 = 0
homensCadastrados = 0
mulheresMenos20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: [F/M] ').strip().upper()
    if sexo in 'MF':
        if sexo == 'M':
            homensCadastrados += 1
        else:
            if idade < 20:
                mulheresMenos20 += 1
        if idade > 18:
            pessoasMais18 += 1
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        if continuar == 'N':
            break
    else:
        print('Cadastro inválido, tente novamente...')
print(f'Há {pessoasMais18} pessoa(s) com mais de 18 anos de idade.')
print(f'Há {homensCadastrados} homem(ns) cadastrado(s).')
print(f'Há {mulheresMenos20} mulher(es) com menos de 20 anos de idade.')
