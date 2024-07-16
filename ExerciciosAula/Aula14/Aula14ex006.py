"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais 
alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos."""

print('=' * 30)
print('     10 TERMOS DE UMA P.A   ')
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
total = 0
escolha = 10

while escolha != 0:
    total = total + escolha
    while cont <= total:
        print('{} '.format(termo), end="-> ")
        termo += razao
        cont += 1
    print('PAUSA')
    escolha = int(input('Gostaria de ver mais quantos termos? [0 - SAIR]: '))

print('Progresão finalizada com {} termos mostrados.'.format(total))
