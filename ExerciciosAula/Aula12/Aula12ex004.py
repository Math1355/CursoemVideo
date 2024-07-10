from datetime import date
atual = date.today().year
ano_nascimento = int(input('Em que ano você nasceu? '))
sexo = str(input('Qual e o seu sexo? '))
idade = atual - ano_nascimento
if sexo == 'M':
    if idade == 18:
        print('Esta no ano de se alistar!')
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print('Você ainda não precisa se alistar, faltam {} anos para se alistar.'.format(saldo))
        print('Você deve se alistar no ano {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        ano = atual - saldo
        print('Você ja deveria ter se alistado! Passou {} anos!'.format(saldo))
        print('Seu alistamento foi em {}'.format(ano))
else:
    print('Você não precisa se alistar!')
