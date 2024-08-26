'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso'''

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
            'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis ', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

numero = int(input("INSIRA O VALOR QUE VOCÊ QUER VER POR EXTENSO [0-20]: "))

while numero not in range(0, 21): 
    numero = int(input("INSIRA O VALOR QUE VOCÊ QUER VER POR EXTENSO [TEM QUE SER ENTRE 0-20]: "))

print(contagem[numero])