# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# # num.pop(2)
# if 4 in num:
#     num.remove(4)
# else:
#     print('Não localizado')
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')


# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for contador in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))

# for chave, valor in enumerate(valores):
#     print(f'Na posição {chave} encontrei  o valor {valor}...')
# print('Cheguei ao final da lista.')


a = [2, 3, 4, 7]
#b = a
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')