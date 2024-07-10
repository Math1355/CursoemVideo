from datetime import date
ano_atual = date.today().year
nascimento = int(input('Qual o ano de nascimento do nadador? '))
idade = ano_atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('A categoria dele e MIRIM')
elif idade <= 14:
    print('A categoria dele e INFANTIL')
elif idade <= 19:
    print('A categoria dele e JUNIOR')
elif idade <= 25:
    print('A categoria dele e SÊNIOR')
else:
    print('A categoria dele e MASTER')
