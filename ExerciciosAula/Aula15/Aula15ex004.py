'''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados 
C) Quantas mulheres tem menos de 20 anos'''

maior_idade = 0
qt_homens = 0
qt_mulheres = 0

while True:
    idade = int(input('INSIRA A IDADE: '))

    while True:
        sexo = str(input('INSIRA O SEXO [M/F]: ')).upper().strip()[0]

        if sexo in 'MmFf':
            break

    if idade >= 18:
        maior_idade += 1

    if sexo in 'Mm':
        qt_homens += 1

    if idade < 20 and sexo in 'Ff':
        qt_mulheres += 1

    while True:
        continuar = str(input('GOSTARIA DE CONTINUAR [S/N]: ')).upper().strip()[0]

        if continuar in 'SsNn':
            break

    if continuar in 'Nn':
        break

print(f'Foram cadastrados {maior_idade} pessoas com mais de 18 anos')
print(f'Foram cadastrados {qt_homens} homens')
print(f'Foram cadastrados {qt_mulheres} mulheres com menos de 20 anos')