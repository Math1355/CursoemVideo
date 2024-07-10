print('=' * 30)
print('    NUMERO PRIMO    ')
print('=' * 30)

valor = int(input ('Insira um valor: '))
resultado = 0

for divisivel in range(1, valor + 1):
    if valor % divisivel == 0:
        print('\033[33m', end=' ')
        resultado += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(divisivel), end=' ')   

print('\n\033[mO número {} foi divisivel {} vezes!'.format(valor, resultado))

if resultado == 2:
    print('{} E UM NUMERO PRIMO!'. format(valor))
else:
    print('{} NÂO E UM NUMERO PRIMO!'. format(valor))