print('=' * 30)
print('     10 TERMOS DE UMA P.A   ')
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao


while termo <= decimo:
    print('{} '.format(termo), end="-> ")
    termo += razao

print('ACABOU')