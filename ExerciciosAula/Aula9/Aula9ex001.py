nome = str(input('Digite um nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas e {}'.format(nome.upper()))
print('Seu nome em minúsculas e {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
dividido = nome.split()
print('Seu primeiro nome e {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))