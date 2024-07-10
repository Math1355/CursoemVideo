from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "pensar" em um numero
print('-=-' * 20)
print('Digite qual numero entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
jogador = (int(input('Qual numero eu pensei? '))) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print('Você acertou!')
else:
    print('Você perdeu! eu pensei em {}'.format(computador))
