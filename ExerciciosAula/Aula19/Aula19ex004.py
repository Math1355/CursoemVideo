'''Crie um programa que gerencia o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador a quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total da gols feitos durante o campeonato.
'''

jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols.')