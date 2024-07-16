'''from math import factorial
n = int(input('INSIRA O VALOR: '))
f = factorial(n)
print('O fatorial de {} e {}.'.format(n, f))'''

valor = int(input('INSIRA O VALOR: '))
contador = valor
fatorial = 1

print('Calculando {}! = '.format(valor), end='')
while contador > 0:
    print('{}'.format(contador), end= '')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
    
#print('O fatorial de {} e: '.format(valor))
print(fatorial)