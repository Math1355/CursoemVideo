print('=' * 20 + 'ARMARINHOS FERNANDIS' + '=' * 20)
valor = float(input('PREÇO DAS COMPRAS? R$ '))
print('''Qual vai ser a forma te pagamento?
[ 1 ] - a vista no dinheiro/cheque
[ 2 ] - a vista cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão''')
opcao = int(input('Digite a opção: '))
if opcao == 1:
    desconto = valor * 0.10
    valor_desconto = valor - desconto
    print('O valor a ser pago com desconto e R$ {:.2f}.'.format(valor_desconto))
elif opcao == 2:
    desconto = valor * 0.05
    valor_desconto = valor - desconto
    print('O valor a ser pago com desconto e R$ {:.2f}.'.format(valor_desconto))
elif opcao == 3:
    parcela = valor / 2
    print('O valor ficou de R$ {:.2f}, parcelado em 2x, então 2x de R$ {:.2f}'.format(valor, parcela))
elif opcao == 4:
    qt_parcelas = int(input('Em quantas vezes vai parcelar? '))
    juros = valor * 0.20
    valor_juros = valor + juros
    parcela = valor_juros / qt_parcelas
    print('O valor ficou de R$ {:.2f}, parcelado em {}x de R$ {:.2f}'.format(valor_juros, qt_parcelas, parcela))
else:
    print('Opção invalida!')
