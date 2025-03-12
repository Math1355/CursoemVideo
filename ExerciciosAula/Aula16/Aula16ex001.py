'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso'''

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze'
            , 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis ', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    while True: 
        numero = int(input("INSIRA O VALOR QUE VOCÊ QUER VER POR EXTENSO [TEM QUE SER ENTRE 0-20]: "))

        if 0 <= numero <= 20:
            break
        print("Tente novamente. ", end='')


    print(f"Você digitou o numero {contagem[numero]}")

    novamente = str(input("Deseja continuar: [S/N] "))

    if novamente[0].upper() ==  "N":
            break
