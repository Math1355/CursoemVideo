print('=' * 30)
print('     CALCULADORA DE PESO   ')
print('=' * 30)

menor = 0
maior = 0

for pessoa in range(1, 6):
    peso = float(input("DIGITE O PESO DA {}ª pessoa: ".format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print("O maior peso foi {} kg".format(maior))
print("O menor peso foi {} kg".format(menor))