'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares'''

n1 = int(input("INSIRA UM VALOR: "))
n2 = int(input("INSIRA UM VALOR: "))
n3 = int(input("INSIRA UM VALOR: "))
n4 = int(input("INSIRA UM VALOR: "))

qt_valor = 0
posicao = 0
valores_pares = []

valores = (n1, n2, n3, n4)

for valor in valores:
    if valor == 9:
        qt_valor += 1

for cont in range(0, len(valores)):
    if valores[cont] == 3:
        posicao = valores.index(3) + 1

print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {qt_valor} vezes')

if posicao != 0:
    print(f'O valor 3 apareceu pela primeira vez na {posicao}º posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')


for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor)

qt_valores_pares = len(valores_pares) - 1


if len(valores_pares) != 0:
    print(f'Os valores pares digitados foram', end=' ')
    
    for valor in valores_pares:
        if valor != valores_pares[qt_valores_pares]:
            print(valor, end=', ')
        else:
            print(valor, end='.')
else:
    print(f'Foram digitados 0 valores pares')
