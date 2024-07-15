"""Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que e a condição de parada. 
No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag)"""

escolha = 0
soma = 0
qt = 0

while escolha != 999:
    novo_valor = int(input('INSIRA UM VALOR [999 - SAIR]: '))
    if novo_valor != 999:
        soma += novo_valor
        qt += 1
    else:
        escolha = 999

print('VOCÊ DIGITOU {} NUMEROS E A SOMA DE TODOS ELES SÃO IGUAL A {}'.format(qt, soma))
