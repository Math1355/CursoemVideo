escolha = 0

while escolha != 5:
    primeiro_numero = int(input('INSIRA O PRIMEIRO NUMERO: '))
    segundo_numero = int(input('INSIRA O SEGUNDO NUMERO: '))
    print('ESCOLHA O QUE DESEJA FAZER')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    escolha = int(input('DIGITE SUA ESCOLHA: '))
    if escolha == 1:
        resultado = primeiro_numero + segundo_numero
        print('O resultado da soma e igual a {}'.format(resultado))
    elif escolha == 2:
        resultado = primeiro_numero * segundo_numero
        print('O resultado da multiplicação e {}'.format(resultado))
    elif escolha == 3:
        resultado = max(primeiro_numero, segundo_numero)
        print('O maior numero e {}'.format(resultado))
    elif escolha == 4:
        escolha = 0
    