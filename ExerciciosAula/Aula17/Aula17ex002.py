'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

numeros = []

while True:
    num = int(input('Digite um número: '))

    if num not in numeros:
        numeros.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Número já existe na lista. Não será adicionado.')

    continuar = input('Deseja continuar? (S/N): ').strip().upper()

    while continuar not in ['S', 'N']:
        continuar = input('Entrada inválida. Deseja continuar? (S/N): ').strip().upper()

    if continuar != 'S':
        break

numeros.sort()
print(f'Os números digitados em ordem crescente são: {numeros}')