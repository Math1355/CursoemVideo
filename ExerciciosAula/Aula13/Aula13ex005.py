valor = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        valor += num
        cont += 1
print('Você informou {} pares. A soma dos valores deu {}'.format(cont, valor))
