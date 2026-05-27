'''Crie um programa onde o usuário possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha 
separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente
'''
numeros = [[], []]

for i in range(7):
    num = int(input(f'Digite o {i + 1}º número: '))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print('-=' * 15)
print(f'Os valores pares são: {sorted(numeros[0])}')
print(f'Os valores ímpares são: {sorted(numeros[1])}')