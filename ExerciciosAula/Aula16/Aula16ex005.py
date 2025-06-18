'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos 
preços na sequência.
No final, mostre uma listagem de preços organizando os dados em forma tabular
Resultado final tem que esta assim:'''

produtos = ("Coca-Cola", 10.50, 
            "Molho-de-Tomate", 1.50, 
            "Leite", 4.50, 
            "Arroz", 24.60, 
            "Oleo", 3.50)

print('-=-' * 20)
print(f'{"MERCADINHO DO DEV PYTHON":^60}')
print('-=-' * 20)

for local in range(0, len(produtos)):
    if local % 2 == 0:
        print(f'{produtos[local]:.<50}', end='')
    else:
        print(f'R$ {produtos[local]:>7.2f}')

print('-=-' * 20)