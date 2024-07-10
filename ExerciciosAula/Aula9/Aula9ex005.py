frase = str(input('Digite uma frase: ')).strip().lower()
#Quantas vezes a letra "A" aparece.
print('A letra "a" aparece {}'.format(frase.count('a')))
#Em que posição ela aparece a primeira vez
print('A letra "a" aparece primeiro na posição {}'.format(frase.find('a')+1))
#Em que posição ela aparece pela última vez
print('A letra "a" aparece por ultimo na posição {}'.format(frase.rfind('a')+1))
