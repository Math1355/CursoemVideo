
lanche = hamburguer <- variavel simples
lanche = Suco             <- variavel simples
'''Vai substituir o hamburguer'''

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

`print(lanche[2])` <- vai mostrar a pizza
`print(lanche[0:2])` <- vai mostrar o hamburguer, suco
`print(lanche[1:])` <- vai mostrar o suco, pizza, pudim
`print(lanche[-1])` <- vai mostrar o pudim
`len(lanche)` <- quantos elementos tem no lanche, 4
`for comida in lanche:` <- vai passar por cada comida da tupla
	`print(comida)`

"As tuplas são IMUTÁVEIS"

DESAFIOS AULA 16
--------------------------------------------

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
R: Aula16ex001.py

Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
R:

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior valor que estão na tupla.
R:

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
R:

Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços organizando os dados em forma tabular
Resultado final tem que esta assim:
![[Pasted image 20240822165027.png]]
R:

Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais, exemplo:
![[Pasted image 20240822165219.png]]
R: