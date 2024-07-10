soma_idade = 0
nome_velho = ""
idade_velho = 0
qt_mulheres20 = 0

for pessoa in range(1, 5):
    print('---- {}ª PESSOA ----'.format(pessoa))
    nome = str(input("NOME: "))
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO (M/F): ")).strip()
    
    soma_idade += idade

    if pessoa == 1 and sexo in 'Mm':
        nome_velho = nome
        idade_velho =  idade
    if sexo in 'Mm' and idade > idade_velho:
        nome_velho = nome
        idade_velho =  idade

    if sexo in 'Ff' and idade < 20:
        qt_mulheres20 += 1

media_idade = soma_idade / 4
print("A media de idade dessas pessoas e {}".format(media_idade))
print("O homem mais velho se chama {} e tem {} anos".format(nome_velho, idade_velho))
print("Temos no total {} mulheres menores de 20 anos".format(qt_mulheres20))