'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos 
preços na sequência.
No final, mostre uma listagem de preços organizando os dados em forma tabular
Resultado final tem que esta assim:'''

produtos = ("Coca-Cola", 10.50, "Molho-de-Tomate", 1.50, "Leite", 4.50, "Arroz", 24.60, "Oleo", 3.50)

print('-=-' * 20)
print(' ' * 20 + 'MERCADINHO DO DEV PYTHON')
print('-=-' * 20)

for local in range(0, len(produtos), 2):
    print(produtos[local].upper(), end='')

    tamanho_produto = len(produtos[local])

    tamanho_ponto = 50 - tamanho_produto 

    print('.' * tamanho_ponto, end=' R$ ')
    print('{:.2f}'.format(produtos[local+1]))

print('-=-' * 20)