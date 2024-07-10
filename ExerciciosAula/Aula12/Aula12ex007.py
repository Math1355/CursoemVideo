print('-=-' * 20)
print('Analisar um triangulo')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos acima PODEM FORMAR um triangulo')
    if r1 == r2 == r3:
        print('O triangulo e um Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('O triangulo e um Escaleno.')
    else:
        print('O triangulo e um Isósceles.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo')

#-Equilátero: todos os lados iguais
#-Isósceles: dois lados iguais
#-Escaleno: todos os lados diferentes