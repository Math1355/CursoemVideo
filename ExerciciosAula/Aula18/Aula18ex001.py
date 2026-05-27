'''Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves.'''

dados_pessoas = []

while True:
    nome = input('Digite o nome da pessoa: ')
    peso = float(input('Digite o peso da pessoa: '))

    dados_pessoas.append([nome, peso])

    resposta = input('Deseja continuar? [S/N] ').strip().upper()

    while resposta not in ['S', 'N']:
        resposta = input('Entrada inválida. Deseja continuar? (S/N): ').strip().upper()

    if resposta == 'N':
        break

print('-=' * 15)
print(f'Foram cadastradas {len(dados_pessoas)} pessoas.')
if dados_pessoas:
    pesos = [p[1] for p in dados_pessoas]
    peso_maximo = max(pesos)
    peso_minimo = min(pesos)

    pessoas_mais_pesadas = [p[0] for p in dados_pessoas if p[1] == peso_maximo]
    pessoas_mais_leves = [p[0] for p in dados_pessoas if p[1] == peso_minimo]

    print(f'As pessoas mais pesadas ({peso_maximo} kg) são: {", ".join(pessoas_mais_pesadas)}')
    print(f'As pessoas mais leves ({peso_minimo} kg) são: {", ".join(pessoas_mais_leves)}')