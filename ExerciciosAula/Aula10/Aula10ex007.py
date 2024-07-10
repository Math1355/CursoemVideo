salario = float(input('Digite o salario do funcionario: R$ '))
if salario <= 1250.00:
    aumento = (salario * 0.15)
    salario = salario + aumento
else:
    aumento = (salario * 0.10)
    salario = salario + aumento
print('O aumento do funcionario e igual a R$ {:.2f}, agora seu salario e R$ {:.2f}'.format(aumento, salario))
