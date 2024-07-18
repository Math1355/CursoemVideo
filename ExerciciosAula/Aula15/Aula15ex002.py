'''Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

while True:
    valor = int(input('DIGITE UM VALOR: [PARA SAIR DIGITE UM VALOR NEGATIVO] '))
    
    if valor < 0:
        break
    
    print('='*30)

    for numero in range(1, 11):
        resultado = valor * numero
        print(f'{valor} x {numero} = {resultado}')
    
    print('='*30)

print('FIM')