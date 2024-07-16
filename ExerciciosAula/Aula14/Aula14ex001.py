
confirmacao = 0
sexo = str(input("INSIRA O SEXO [M/F]: ")).strip().upper()[0]

'''while sexo not in "MnFf":
    sexo = sexo = str(input("INSIRA O SEXO [M/F]: ")).strip().upper()[0]'''

while confirmacao != 1:
    if sexo == 'M' or sexo == 'F':
        confirmacao = 1    
    else:
        sexo = str(input("Dados incorreto. Por favor informe seu sexo [M/F]: ")).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sexo))