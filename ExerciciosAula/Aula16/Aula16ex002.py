'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Fluminense.'''

brasileiro = ('Fortaleza', 'Botafogo', 'Palmeiras', 'Flamengo', 'São Paulo', 'Bahia', 'Cruzeiro', 
              'Atlético-MG', 'Athelico Paranaense', 'Vasco', 'Internacional', 'Juventude', 'Grêmio', 
              'Bragantino', 'Criciúma', 'Fluminense', 'Vitória', 'Corinthians', 'Cuiabá', 'Atlético-GO')

print(f'Os primeiros 5 colocados são: {0:5}')
print(f'A lista de times em ordem alfabética:')
for time in brasileiro:
    print(f'{time}')
print(f'O Fluminense esta na posição {brasileiro.index('Fluminense') + 1}')
