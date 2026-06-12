'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastra-os (com idade) 
em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. (35 anos)
'''
from datetime import date

dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['contratacao'] + 35 - nascimento

print('-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}.')

# print(f'Nome: {dados["nome"]}')
# print(f'Idade: {dados["idade"]} anos')
# if dados['ctps'] != 0:
#     print(f'Carteira de trabalho: {dados["ctps"]}')
#     print(f'Ano de contratação: {dados["contratacao"]}')
#     print(f'Salário: R${dados["salario"]:.2f}')
#     print(f'Idade para aposentadoria: {dados["aposentadoria"]} anos')