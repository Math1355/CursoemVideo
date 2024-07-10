peso = float(input('Digite um peso: (kg) '))
altura = float(input('Digite uma altura: (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você esta abaixo do Peso.')
elif imc <= 25:
    print('Você esta no Peso ideal.')
elif imc <= 30:
    print('Você esta Sobrepeso.')
elif imc <= 40:
    print('Você esta com Obesidade')
else:
    print('Voce esta com Obesidade mórbida')

#-Abaixo de 18.5: Abaixo do Peso
#-Entre 18.5 e 25: Peso ideal
#-25 ate 30: Sobrepeso
#-30 ate 40: Obesidade
#-Acima de 40: Obesidade mórbida