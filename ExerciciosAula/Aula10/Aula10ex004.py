km = float(input('Qual a distancia da viagem em KM? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(km))
preco = km * 0.50 if km <= 200 else km * 0.45
'''if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45'''
print('O valor da passagem e R$ {:.2f}'.format(preco))
