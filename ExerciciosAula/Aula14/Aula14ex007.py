'''Escreva um programa que leia um numero n inteiro 
qualquer e mostre na tela os n primeiros elementos 
de um Sequência de Fubonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 ->8'''

valor = int(input('INSIRA UM VALOR: '))
primeiro_valor = 0
segundo_valor = 1



while valor != 0:
    if primeiro_valor == 0:
        print('{} '.format(primeiro_valor), end="-> ")
        print('{} '.format(segundo_valor), end="-> ")
        valor -= 2

    novo_valor = primeiro_valor + segundo_valor
    print('{} '.format(novo_valor), end="-> ")
    
    valor -= 1
    primeiro_valor = segundo_valor
    segundo_valor = novo_valor

print('ACABOU')