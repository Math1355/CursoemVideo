from datetime import date

print('=' * 30)
print('     CALCULADORA DE IDADE   ')
print('=' * 30)

qt_maior = 0
qt_menor = 0
ano_atual = date.today().year


for pessoa in range(1, 8):
    ano =  int(input("DIGITA UM ANO DE NASCIMENTO da {}ª pessoa: ".format(pessoa)))
    idade = ano_atual - ano
    if idade >= 21:
        qt_maior += 1
    else:
        qt_menor += 1

print("Ao todo tivemos {} pessoas maiores de idade".format(qt_maior))
print("Ao todo tivemos {} pessoas menores de idade".format(qt_menor))