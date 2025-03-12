'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior valor que estão na 
tupla.'''
from random import randint

valores = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))

print('Os valores sorteados foram: ', end='')
for n in valores:
    print(f'{n} ', end='')
    
print(f'\nO MAIOR VALOR FOI: {max(valores)}')
print(f'O MENOR VALOR FOI: {min(valores)}')