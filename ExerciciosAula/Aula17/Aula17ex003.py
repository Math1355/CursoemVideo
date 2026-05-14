'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
'''

numero_1 = int(input("Digite um valor: "))
numero_2 = int(input("Digite um valor: "))
numero_3 = int(input("Digite um valor: "))
numero_4 = int(input("Digite um valor: "))
numero_5 = int(input("Digite um valor: "))

lista_numeros = []

for numero in [numero_1, numero_2, numero_3, numero_4, numero_5]:
    if not lista_numeros:
        lista_numeros.append(numero)
    else:
        for i in range(len(lista_numeros)):
            if numero < lista_numeros[i]:
                lista_numeros.insert(i, numero)
                break
        else:
            lista_numeros.append(numero)

print(f'Os números digitados em ordem crescente são: {lista_numeros}')