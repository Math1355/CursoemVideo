'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar. 
No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$ 1000
C) Qual é o nome do produto mais barato.'''

total = 0
qt_caro = 0

while True:
    produto = str(input('INSIRA O NOME DO PRODUTO: '))
    preco = float(input('INSIRA O PREÇO DO PRODUTO: '))

    if total == 0:
        valor_barato = preco
        produto_barato = produto
    else:
        if preco < valor_barato:
            valor_barato = preco
            produto_barato = produto    

    total += preco

    if preco > 1000:
        qt_caro += 1

    while True:
        continuar = str(input('GOSTARIA DE CONTINUAR [S/N]: ')).upper().strip()[0]

        if continuar in 'SsNn':
            break
    
    if continuar in 'Nn':
        break

print(f'O TOTAL DA COMPRA FOI DE {total:.2f}')
print(f'VOCÊ COMPROU {qt_caro} PRODUTOS ACIMA DE R$ 1000,00! GANHARA UM DESCONTO')
print(f'O PRODUTO MAIS BARATO QUE VOCÊ COMPROU FOI {produto_barato.upper()}')