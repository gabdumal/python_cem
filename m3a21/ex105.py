titulo = 'Notas de alunos'
numTitulo = len(titulo)
numTituloDet = (numTitulo // 3) + 1
print('\033[33m-=-\033[m' * numTituloDet)
print(f'\033[33m{titulo.upper():^{numTituloDet * 3}}\033[m')
print('\033[33m-=-\033[m' * numTituloDet)


# Funções
def notas(* nota, sit=False):
    """
    -> Cria uma função para analisar notas e situação de vários alunos.
    :param nota: Nota de um aluno.
    :param sit: (opcional) Situação geral da turma, se Boa, razoável ou ruim.
    :return: O dicionário com o total de notas registradas, a maior nota, a menor nota, a média das notas e a
    situação geral se solicitado.
    """
    maior = nota[0]
    menor = nota[0]
    soma = 0
    for n in nota:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        soma += n
        comprimento = len(nota)
        media = soma / comprimento
    lista = {'total': comprimento, 'maior': maior, 'menor': menor, 'media': media}
    if sit:
        if media >= 7:
            situacao = 'BOA'
        elif 4 < media < 7:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'RUIM'
        lista.update({'situacao': situacao})
    return lista


# Programa principal
resp = notas(3, 7.5, 8.9, 6.7, 3.6, 9.8, 8.9, 9.2, sit=True)
print(resp)
