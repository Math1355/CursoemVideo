'''Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

alunos = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()

    while resposta not in ['S', 'N']:
        resposta = input('Entrada inválida. Deseja continuar? (S/N): ').strip().upper()

    if resposta == 'N':
        break

print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)
for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('-' * 26)

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 para sair) '))

    if opcao == 999:
        print('Finalizando...')
        break

    if 0 <= opcao < len(alunos):
        print(f'Notas de {alunos[opcao][0]} são: {alunos[opcao][1]}')
    else:
        print('Opção inválida. Tente novamente.')