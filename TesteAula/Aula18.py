teste = list()
teste.append('Matheus')
teste.append(26)
print(teste)

galera = list()
galera.append(teste[:])
print(galera)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera_nova = [['Matheus', 26], ['Maria', 22], ['João', 19], ['Ana', 32]]
print(galera_nova)
print(galera_nova[0])
print(galera_nova[0][0])
print(galera_nova[2][1])

for pessoa in galera_nova:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

galera_input = list()
dado = list()
for contador in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera_input.append(dado[:])
    dado.clear()

print(galera_input)

total_maior = total_menor = 0

for pessoa in galera_input:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        total_menor += 1

print(f'Temos {total_maior} maiores de idade e {total_menor} menores de idade.')