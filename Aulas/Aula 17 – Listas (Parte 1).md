`lanche = ('hamburguer', 'suco'. 'pizza', 'pudim') <- Isso e uma tupla
`print(lanche[2]) <- pizza
`lanche[3] = 'picole' <- da erro porque uma tupla e imutavel

Para mudar um atributo precisa utilizar uma **lista**

`Tuplas = ()
`Lista = []

`lanche = ['hamburguer', 'suco'. 'pizza', 'pudim'] <- Isso e uma lista
`lanche[3] = 'picole' <- da certo

Ambas são variáveis compostas mas o que muda e que a tupla não muda, a lista muda

Para adicionar na lista um elemento novo:
`lanche.append('bolacha')
`lanche.insert(0, 'cachorro-quente') <- adiciona antes do hamburguer

Para apagar os elementos:
`del lanche[3]
`lanche.pop(3)
`lanche.remove('pizza')
`lanche.pop() <- Remove o ultimo elemento

Após isso o próximo elemento ficará no lugar daquele que você deletou.
Se tentar remover um elemento que ja foi removido, dará erro

`if 'pizza' inlanche:
	`lanche.remove('pizza')

`valores = list(range(4, 11))
`valores = [8, 2, 5, 4, 9, 3, 0]
`valores.sort() <- vai ordenar todos os valores
`valores.sort(reverse=True) <- Vai ordenar de forma invertida
`len(valores) <- quantos elementos tem na lista

Resultado: `[4, 5, 6, 7, 8, 9, 10]


DESAFIOS AULA 17
--------------------------------------------

Faça um programa que leia **5 valores numéricos** e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
R: Aula17ex001.py

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
R: Aula17ex002.py

Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
R: Aula17ex003.py

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A)Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C)Se o valor 5 foi digitado e está ou não na lista.
R: Aula17ex004.py

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
R: Aula17ex005.py

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
R: Aula17ex006.py




