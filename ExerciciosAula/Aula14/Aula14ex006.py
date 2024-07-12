"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais 
alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos."""

print('=' * 30)
print('     10 TERMOS DE UMA P.A   ')
print('=' * 30)

escolha = 10
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (escolha - 1) * razao

while termo <= decimo:
    print('{} '.format(termo), end="-> ")
    termo += razao
    if termo == decimo:
        escolha = int(input('\nGostaria de ver mais quantos termos? [0 - SAIR]: '))
        decimo = termo + (escolha - 1) * razao

print('ACABOU')