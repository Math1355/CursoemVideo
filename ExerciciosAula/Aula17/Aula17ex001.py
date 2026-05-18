'''Faça um programa que leia **5 valores numéricos** e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista_numeros = []
maior = menor = 0

for contagem in range(0, 5 ):
    lista_numeros.append(int(input(f"Digite um valor para a posição {contagem}: ")))
    if contagem == 0:
        maior = menor = lista_numeros[contagem]
    else:
        if lista_numeros[contagem] > maior:
            maior = lista_numeros[contagem]
        if lista_numeros[contagem] < menor:
            menor = lista_numeros[contagem]

print("=-=" * 15)
print(f"Você digitou os valores: {lista_numeros}")
print(f"O maior valor digitado foi {maior} na posição ", end="")
for index, valor in enumerate(lista_numeros):
    if valor == maior:
        print(f"{index}... ", end="")
print()  # Quebra de linha
print(f"O menor valor digitado foi {menor} na posição ", end="")
for index, valor in enumerate(lista_numeros):
    if valor == menor:
        print(f"{index}... ", end="")
print()  # Quebra de linha
