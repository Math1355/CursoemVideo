"""Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valor lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores"""

qt = 0
escolha = 1
resultado = 0


while escolha == 1:
    valor = int(input('INSIRA UM VALOR: '))
    if qt == 0:
        menor_valor = valor
        maior_valor = valor
    else:
        if valor <= menor_valor:
            menor_valor = valor
        else:
            maior_valor = valor

    qt += 1
    resultado += valor
    escolha = int(input('GOSTARIA DE CONTINUAR [1 - SIM / 0 - NÃO]? '))

media = resultado / qt

print('A MEDIA DO VALORES QUE VOCÊ DIGITOU E DE {:.2f}'.format(media))
print('O MENOR VALOR QUE VOCÊ DIGITOU FOI {} E O MAIOR VALOR FOI {}'.format(menor_valor, maior_valor))
