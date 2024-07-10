'''for c in range(6, 0, -1):
    print(c)
print('fim')

for c in range(0, 7, 2):
    print(c)
print('fim')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos valores foi de {}'.format(s))
