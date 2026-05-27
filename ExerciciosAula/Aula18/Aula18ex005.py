'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint
import time

print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)

jogos = list()
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))

for contador in range(0, quantidade):
    jogo = list()
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogos.append(jogo[:])
    jogo.clear()

print('-' * 30)
print(f"      SORTEANDO {quantidade} JOGOS!")

for i, jogo in enumerate(jogos):
    time.sleep(1)
    print(f'Jogo {i+1}: {sorted(jogo)}')

print('      BOA SORTE!')
print('-' * 30)