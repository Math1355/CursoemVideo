print('=' * 30)
print('     10 TERMOS DE UMA P.A   ')
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1


while cont <= 10:
    print('{} '.format(termo), end="-> ")
    termo += razao
    cont += 1

print('ACABOU')