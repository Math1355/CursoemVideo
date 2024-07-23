'''Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''
print('='*30)
print('TABUADA')
print('='*30)

while True:
    valor = int(input('DIGITE UM VALOR: [PARA SAIR DIGITE UM VALOR NEGATIVO] '))
    
    print('='*30)
    
    if valor < 0:
        break 

    for numero in range(1, 11):
        print(f'{valor} x {numero} = {valor * numero}')
    
    print('='*30)
    print('SE QUISER CONTINUAR')

print('FIM')