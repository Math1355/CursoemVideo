'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados. OK
B) Os últimos 4 colocados da tabela. OK
C) Uma lista com os times em ordem alfabética. OK
D) Em que posição na tabela está o time da Fluminense. OK'''

brasileiro = ('Fortaleza', 'Botafogo', 'Palmeiras', 'Flamengo', 'São Paulo', 'Bahia', 'Cruzeiro', 
              'Atlético-MG', 'Athelico Paranaense', 'Vasco', 'Internacional', 'Juventude', 'Grêmio', 
              'Bragantino', 'Criciúma', 'Fluminense', 'Vitória', 'Corinthians', 'Cuiabá', 'Atlético-GO')

lista_alfabetica = []

print(f'Os primeiros 5 colocados são: {brasileiro[0:5]}')

print(f'Os 4 útlimos colocados são: {brasileiro[-4:]}')

for time in brasileiro:
    lista_alfabetica.append(time)

print(f'A lista de times em ordem alfabética: {sorted(lista_alfabetica)}')

print(f'O Fluminense esta na posição {brasileiro.index('Fluminense') + 1}')
