'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A)Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C)Se o valor 5 foi digitado e está ou não na lista.
'''

lista_numeros = []

while True:
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)

    continuar = input('Deseja continuar? (S/N): ').strip().upper()

    while continuar not in ['S', 'N']:
        continuar = input('Entrada inválida. Deseja continuar? (S/N): ').strip().upper()

    if continuar != 'S':
        break

print(f'A) Quantos números foram digitados: {len(lista_numeros)}')

lista_numeros.sort(reverse=True)
print(f'B) A lista de valores, ordenada de forma decrescente: {lista_numeros}')

if 5 in lista_numeros:
    print('C) O valor 5 foi digitado e está na lista.')
else:
    print('C) O valor 5 não foi digitado ou não está na lista.')