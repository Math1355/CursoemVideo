'''Crie um programa que leia nome, Sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário a todos os dicionários em uma lista. No final, mostra: 
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo. 
C) Uma lista com todas as mulheres. 
D) Uma lista com todas as pessoas com idade acima da média.
'''

pessoas = []
while True:
    pessoa = {}

    pessoa['nome'] = str(input('Nome: ')).strip()

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]

        if pessoa['sexo'] in 'MF':
            break

        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))

    pessoas.append(pessoa)

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if resp in 'SN':
            break

        print('ERRO! Responda apenas S ou N.')
        
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

media_idade = sum(p['idade'] for p in pessoas) / len(pessoas)
print(f'B) A média de idade do grupo é de {media_idade:.2f} anos.')

print('C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas com idade acima da média: ')
for p in pessoas:
    if p['idade'] > media_idade:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
