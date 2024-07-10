nome = str(input("Qual é o seu nome? "))
if nome == 'Matheus':
    print('Que nome bonito!')
elif nome == 'Bia' or nome == 'Enzo' or nome == 'Luiz':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}'.format(nome))
