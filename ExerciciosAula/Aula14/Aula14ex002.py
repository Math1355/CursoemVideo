from random import randint
from time import sleep

computador = randint(1, 10)
print('-=-' * 20)
print('Digite qual numero entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)

chute = 11
palpites = 0

while chute != computador:
    chute = int(input('Qual numero eu pensei? '))
    print('PROCESSANDO...')
    sleep(2)
    if chute == computador:
        print('Você acertou!')
    else:
        print('Você errou! tente novamente!')
        palpites += 1

print('VOCÊ ERROU {} VEZES!'.format(palpites))