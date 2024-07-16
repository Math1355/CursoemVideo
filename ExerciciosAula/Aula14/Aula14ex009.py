"""Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valor lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores"""

qt = resultado = media = menor_valor = maior_valor = 0
escolha = 'S'


while escolha in 'Ss':
    valor = int(input('INSIRA UM VALOR: '))
    if qt == 1:
        menor_valor = valor
        maior_valor = valor
    else:
        if valor > maior_valor:
            maior_valor = valor
        if valor < menor_valor:
            menor_valor = valor

    qt += 1
    resultado += valor
    escolha = str(input('GOSTARIA DE CONTINUAR [S/N]? ')).upper().strip()[0]

media = resultado / qt

print('VOCÊ DIGITOU {} NUMERO.'.format(qt))
print('A MEDIA DO VALORES QUE VOCÊ DIGITOU E DE {:.2f}'.format(media))
print('O MENOR VALOR QUE VOCÊ DIGITOU FOI {} E O MAIOR VALOR FOI {}'.format(menor_valor, maior_valor))
