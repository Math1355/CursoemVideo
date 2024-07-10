'''nome = str(input('Qual e o seu nome? '))
if nome == 'Matheus':
    print('Belo nome!')
else:
    print('Seu nome e normal')
print('Bom dia, {}!'.format(nome))'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m= (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
'''if m >= 6.0:
    print('Sua media foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')'''
print('PARABENS' if m>= 6.0 else 'ESTUDE MAIS!')

