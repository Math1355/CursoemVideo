
confirmacao = 0

while confirmacao != 1:
    sexo = str(input("INSIRA O SEXO [M/F]: ")).upper()
    if sexo == 'M' or sexo == 'F':
        confirmacao = 1    

print('FIM')