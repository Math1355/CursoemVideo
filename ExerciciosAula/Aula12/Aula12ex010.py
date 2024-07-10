from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
aleatorio = randint(0, 2)
print('=' * 20 + 'JOKENPÔ' + '=' * 20)
print('''Faça sua escolha
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
escolha = int(input('Sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-=' * 20)
print('''A maquina escolheu {}
O Jogador escolheu {}'''.format(itens[aleatorio], itens[escolha]))
print('-=' * 20)
if aleatorio == 0:
    if escolha == 0:
        print('EMPATE!')
    elif escolha == 1:
        print('Você ganhou!')
    elif escolha == 2:
        print('Você perdeu')
    else:
        print('JOGADA INVALIDA')
elif aleatorio == 1:
    if escolha == 0:
        print('Você perdeu')
    elif escolha == 1:
        print('EMPATE!')
    elif escolha == 2:
        print('Você ganhou!')
    else:
        print('JOGADA INVALIDA')
elif aleatorio == 2:
    if escolha == 0:
        print('Você ganhou!')
    elif escolha == 1:
        print('Você perdeu')
    elif escolha == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA')