'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior valor que estão na tupla.'''
from random import randint

valor_1 = randint(0, 20) 
valor_2 = randint(0, 20)
valor_3 = randint(0, 20)
valor_4 = randint(0, 20)
valor_5 = randint(0, 20)

valores = (valor_1, valor_2, valor_3, valor_4, valor_5)

print(valores)
print(f'O MAIOR VALOR FOI: {max(valores)}')
print(f'O MENOR VALOR FOI: {min(valores)}')