'''Faça um programa que jogue par ou impar com o computador. 
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
from time import sleep


print('-=-' * 20)
print('PAR OU IMPAR')
print('-=-' * 20)

qt = 0

while True:
    computador = randint (1, 10)
    valor = int(input('DIGITE UM VALOR: '))

    while True:
        escolha = str(input('PAR OU IMPAR: ')).upper().strip()[0]
        if escolha == 'P'  :
            escolha_comp = 'I'
            break
        elif escolha == 'I':
            escolha_comp = 'P'
            break

    soma = computador + valor

    sleep(2)

    if soma % 2 == 0:
        if escolha == 'P':
            print(f'VOCÊ JOGOU {valor} E O COMPUTADOR {computador}. TOTAL {soma} DEU PAR')
            print('PARABENS VOCÊ GANHOU DO COMPUTADOR!.')
            qt += 1
        elif escolha_comp == 'P':
            print(f'VOCÊ JOGOU {valor} E O COMPUTADOR {computador}. TOTAL {soma} DEU PAR')
            break
    else:
        if escolha == 'I':
            print(f'VOCÊ JOGOU {valor} E O COMPUTADOR {computador}. TOTAL {soma} DEU IMPAR')
            print('PARABENS VOCÊ GANHOU DO COMPUTADOR!.')
            qt += 1
        elif escolha_comp == 'I':
            print(f'VOCÊ JOGOU {valor} E O COMPUTADOR {computador}. TOTAL {soma} DEU IMPAR')
            break

    print('-=-' * 20)

print('-=-' * 20)
print(f'VOCÊ PERDEU! SUA SEQUENCIA DE VITORIAS FOI {qt}!')
