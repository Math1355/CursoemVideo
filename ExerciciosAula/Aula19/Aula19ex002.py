'''
Crie um programa onda 4 jogadores joguem um dado a tenham resultados aleatórios. Guarda esses resultados em um dicionário.
No final, coloque asse dicionário em ordem. sabendo que o vencedor tirou o maior número no dado.
'''
import random
from time import sleep
from operator import itemgetter

jogadores = {}
for i in range(1, 5):
    jogadores[f'jogador{i}'] = random.randint(1, 20)

print('Resultados dos jogadores:')
for jogador, resultado in jogadores.items():
    print(f'{jogador} tirou: {resultado} no dado.')
    sleep(1)

ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('=-' * 30)
print('\nRanking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com o número {v[1]}')
    sleep(1)

vencedor = ranking[0][0]
print(f'\nO vencedor é {vencedor} com o número {jogadores[vencedor]}!')