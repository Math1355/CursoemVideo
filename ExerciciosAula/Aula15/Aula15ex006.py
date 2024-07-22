'''R:Crie um programa que simule o funcionamento de um caixa eletrônico. 
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''
print('=' * 30)
print('     BANCO CEV   ')
print('=' * 30)

valor = int(input('INSIRA O VALOR QUE GOSTARIA DE SACAR: R$ '))

qt_50 = 0
qt_20 = 0
qt_10 = 0
qt_1 = 0

while valor != 0:
    while valor >= 50:
        qt_50 += 1
        valor -= 50
    
    while valor >= 20:
        qt_20 += 1
        valor -= 20

    while valor >= 10:
        qt_10 += 1
        valor -= 10
    
    while valor >= 1:
        qt_1 += 1
        valor -= 1

    

print(f'Total de {qt_50} cédulas de R$50')
print(f'Total de {qt_20} cédulas de R$20')
print(f'Total de {qt_10} cédulas de R$10')
print(f'Total de {qt_1} cédulas de R$1')
print('=' * 30)
print(f'Volte sempre ao BANCO CEV! Tenha um bom dia!')
