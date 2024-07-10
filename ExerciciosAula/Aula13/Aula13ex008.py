print('=' * 30)
print('     PALÍNDROMO   ')
print('=' * 30)

frase = str(input("DIGITE A FRASE: ")).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} e {}'.format(junto, inverso))

if junto == inverso:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palíndromo!')

'''frase = str(input("DIGITE A FRASE: ")).lower().strip()
frase_reverse =  frase[::-1]


if frase.replace(" ", "") == frase_reverse.replace(" ", ""):
    print("{} E UM PALÍNDROMO".format(frase.upper()))
else:
    print("{} NÃO E UM PALÍNDROMO".format(frase.upper()))'''