'''cont = 1

while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

nome = 'Jose'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos.')
print('O {} tem {} anos.'.format(nome, idade))
print(f'O {} tem {} anos e ganha R$ {salario:.2f}.')
'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

#print('A soma vale {}'.format(s))
print(f'A soma valoe {s}')
