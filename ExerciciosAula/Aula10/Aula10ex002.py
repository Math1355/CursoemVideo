velocidade = float(input('Qual foi a velocidade do carro em Km? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você ultrapassou o limite de 80 KM!')
    print('Sua multa e no valor de R$ {:.2f}'.format(multa))
else:
    print('Você esta dentro do limite da velocidade!')