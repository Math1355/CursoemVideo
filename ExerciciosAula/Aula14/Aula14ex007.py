'''Escreva um programa que leia um numero n inteiro 
qualquer e mostre na tela os n primeiros elementos 
de um Sequência de Fubonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 ->8'''

''' #feito por mim
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

print('ACABOU')'''
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

valor = int(input('Quantos termos você quer ver?: '))
t1 = 0
t2 = 1
cont = 3

print('~'*30)
print('{} -> {}'.format(t1, t2), end='')

while cont <= valor:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1 

print(' -> FIM')
