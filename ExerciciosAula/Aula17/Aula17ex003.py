'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
'''
lista_numeros = []

for contador in range (0, 5):
    valor = int(input("Digite um valor: "))
    if contador == 0 or valor > lista_numeros[-1]:
        lista_numeros.append(valor)
        print("Adicionado no final da lista...")
    else:
        pos = 0
        while pos < len(lista_numeros):
            if valor <= lista_numeros[pos]:
                lista_numeros.insert(pos, valor)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1

print(f'Os números digitados em ordem crescente são: {lista_numeros}')