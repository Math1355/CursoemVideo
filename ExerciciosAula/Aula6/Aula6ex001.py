n1 = int(input('\033[7;30mDigite um numero:\033[m '))
n2 = int(input('\033[7;30mDigite outro numero:\033[m '))
soma = n1 + n2
print('O resultado da soma: \033[0;31m{}\033[m + \033[0;31m{}\033[m = \033[0;31m{}\033[m'.format(n1, n2, soma))
