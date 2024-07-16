

primeiro_numero = int(input('INSIRA O PRIMEIRO NUMERO: '))
segundo_numero = int(input('INSIRA O SEGUNDO NUMERO: '))
escolha = 0

while escolha != 5:
    print('''ESCOLHA O QUE DESEJA FAZER
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    escolha = int(input('DIGITE SUA ESCOLHA: '))
    if escolha == 1:
        resultado = primeiro_numero + segundo_numero
        print('O resultado da soma de {} e {} e igual a {}'.format(primeiro_numero, segundo_numero, resultado))
    elif escolha == 2:
        resultado = primeiro_numero * segundo_numero
        print('O resultado da multiplicação de {} e {} e igual a {}'.format(primeiro_numero, segundo_numero, resultado))
    elif escolha == 3:
        resultado = max(primeiro_numero, segundo_numero)
        print('O maior numero entre {} e {} e igual a {}'.format(primeiro_numero, segundo_numero, resultado))
    elif escolha == 4:
        print('Informe os números novamente:')
        primeiro_numero = int(input('INSIRA O PRIMEIRO NUMERO: '))
        segundo_numero = int(input('INSIRA O SEGUNDO NUMERO: '))
    elif escolha == 5:
        print('FIM DO PROGRAMA!')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)

