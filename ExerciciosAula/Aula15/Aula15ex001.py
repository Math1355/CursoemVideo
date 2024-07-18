'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que e a condição de parada. 
No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag)'''

qt = total = 0

while True:
    valor = int(input('DIGITE UM NUMERO: [999 PARA SAIR] '))
    if valor == 999:
        break
    total += valor
    qt += 1

print(f'VOCÊ DIGITOU {qt} NUMEROS E A SOMA DESSES VALORES E IGUAL A {total}')