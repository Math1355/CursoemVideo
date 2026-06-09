'''
Faça um programa que leia nome e média de um aluno. guardando também a situação em um dicionário. No final, mostra o conteúdo da estrutura na tela.
'''

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print('-=' * 30)
print(f'Situação do aluno {aluno["nome"]}:\nMédia: {aluno["media"]}\nSituação: {aluno["situacao"]}')