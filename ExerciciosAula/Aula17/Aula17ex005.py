'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    
    if num not in lista:
        lista.append(num)
    else:
        print('Número já existe na lista. Digite outro número.')
    
    resposta = input('Quer continuar? [S/N] ').strip().upper()

    while resposta not in ['S', 'N']:
        resposta = input('Entrada inválida. Deseja continuar? (S/N): ').strip().upper()
    
    if resposta == 'N':
        break

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("=-=" * 15)
print(f'Lista completa: {lista}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')
