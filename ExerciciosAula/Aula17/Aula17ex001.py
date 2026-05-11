'''Faça um programa que leia **5 valores numéricos** e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

numero_1 = int(input("Digite um valor para a posição 0: "))
numero_2 = int(input("Digite um valor para a posição 1: "))
numero_3 = int(input("Digite um valor para a posição 2: "))
numero_4 = int(input("Digite um valor para a posição 3: "))
numero_5 = int(input("Digite um valor para a posição 4: "))

lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]

print("=-=" * 15)
print(f"Você digitou os valores: {lista_numeros}")
print(f"O maior valor digitado foi {max(lista_numeros)} na posição {lista_numeros.index(max(lista_numeros))}")
print(f"O menor valor digitado foi {min(lista_numeros)} na posição {lista_numeros.index(min(lista_numeros))}")