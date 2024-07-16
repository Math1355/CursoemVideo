from random import randint
from time import sleep

computador = randint(1, 10)
print('-=-' * 20)
print('Digite qual numero entre 0 e 10. Tente adivinhar... ')
print('-=-' * 20)

acertou = False
palpites = 0

while not acertou:
    chute = int(input('Qual numero eu pensei? '))
    print('PROCESSANDO...')
    sleep(2)
    palpites += 1
    if chute == computador:
        print('Você acertou!')
        acertou = True
    else:
        if chute < computador:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente!')
        

print('VOCÊ ACERTOU COM {} TENTATIVAS, PARABENS!'.format(palpites))
