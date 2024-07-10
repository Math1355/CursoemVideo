valor = float(input('Insira o valor do imovel: '))
salario = float(input('Insira o salario: '))
anos = int(input('Em quantos anos vai ser pago o imovel: '))
valor_parcela = valor / (anos * 12)
porcentagem_renda = salario * 0.30
if valor_parcela <= porcentagem_renda:
    print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}.'.format(valor, anos, valor_parcela))
    print('Empréstimo pode ser CONVEDIDO!')
else:
    print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}.'.format(valor, anos, valor_parcela))
    print('Empréstimo NEGADO!')
