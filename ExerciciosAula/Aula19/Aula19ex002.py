'''
Crie um programa onda 4 jogadores joguem um dado a tenham resultados aleatórios. Guarda esses resultados em um dicionário.
No final, coloque asse dicionário em ordem. sabendo que o vencedor tirou o maior número no dado.
'''
import random

jogadores = {}
for i in range(1, 5):
    jogadores[f'jogador{i}'] = random.randint(1, 20)

print('Resultados dos jogadores:')
for jogador, resultado in jogadores.items():
    print(f'{jogador}: {resultado}')

vencedor = max(jogadores, key=jogadores.get)
print(f'\nO vencedor é {vencedor} com o número {jogadores[vencedor]}!')