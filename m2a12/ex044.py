print('-=-' * 6)
print('CÁLCULO DE PREÇO')
print('-=-' * 6)
precoNormal = float(input('Digite o preço normal: R$ '))
print('PAGAMENTOS')
print(' [1] À vista no dinheiro ou cheque\n [2] À vista no cartão')
print(' [3] 2x no cartão\n [4] 3x ou mais no cartão')
condicaoPagamento = int(input('Selecione a condição de pagamento: '))

if condicaoPagamento == 1:
    print('Preço com 10% de desconto: R$ {:.2f}'.format(precoNormal * 0.9))
elif condicaoPagamento == 2:
    print('Preço com 5% de desconto: R$ {:.2f}'.format(precoNormal * 0.95))
elif condicaoPagamento == 3:
    print('Preço normal: R$ {:.2f}'.format(precoNormal))
elif condicaoPagamento == 4:
    print('Preço com 20% de juros: R$ {:.2f}'.format(precoNormal * 1.2))
else:
    print('A opção selecionada é inválida.')
