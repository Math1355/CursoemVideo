valor = int(input('INSIRA O VALOR: '))
resultado = 0

print('O fatorial de {} e: '.format(valor))

while valor != 1:
    segundo_valor = valor - 1
    if resultado == 0:
        resultado = valor * segundo_valor 
        valor -= 2
    else:
        resultado = resultado * valor
        valor -= 1    
    

print(resultado)