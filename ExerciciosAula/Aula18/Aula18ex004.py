'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A Soma dos valores da terceira coluna.
C) O maior valor da segunda linha'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 15)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

soma_pares = soma_terceira_coluna = maior_segunda_linha = 0

for linha in range(3):
    for coluna in range(3):
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]

        if linha == 1:
            if matriz[linha][coluna] > maior_segunda_linha:
                maior_segunda_linha = matriz[linha][coluna]

print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')