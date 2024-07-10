n1 = float(input('Escreva a primeira nota: '))
n2 = float(input('Escreva a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua media foi de {:.2f}, abaixo de 5.0, Você foi reprovado.'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua media foi de {:.2f}, você esta de recuperação.'.format(media))
elif media >= 7.0:
    print('Sua media foi de {:.2f}, você foi aprovado!'.format(media))
