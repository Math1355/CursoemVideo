lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#tuplas são imutáveis
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

#lanche[1] = 'Refrigerante' Vai da erro

#for comida in lanche:
#    print(f'Eu vou comer {comida}') # NÃO TEM A POSIÇÃO
print(len(lanche))
#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}') # PARA TER A POSIÇÃO
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') # PARA TER A POSIÇÃO

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = a + b # NÃO E A MESMA COISA QUE b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))

pessoa = ('Matheus', 24, 'M', 60.00)
print(pessoa)
del(pessoa) #apaga a variavel