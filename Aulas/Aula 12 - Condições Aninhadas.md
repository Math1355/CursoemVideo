carro.siga()
se carro.esquerda()
	carro.siga() <- bloco verdadeiro
	carro.direita()
	carro.siga()
	carro.direita()
	carro.esquerda()
	carro.siga()
	carro.direita()
	carro.siga()
senão se carro.direita()
	carro.siga() <- bloco falso
	carro.esquerda()
	carro.siga()
	carro.esquerda()
	carro.siga()
senão
	carro.siga()
carro.pare()

carro.siga()
if carro.esquerda():
	carro.siga() <- bloco verdadeiro
	carro.direita()
	carro.siga()
	carro.direita()
	carro.esquerda()
	carro.siga()
	carro.direita()
	carro.siga()
elif carro.direita():
	carro.siga() <- bloco falso
	carro.esquerda()
	carro.siga()
	carro.esquerda()
	carro.siga()
else:
	carro.siga()
carro.pare()

Estrutura:

if carro.esquerda():

elif carro.direita(): == else if carro.direita();

elif carro.ré():

else:

DESAFIOS AULA 12
--------------------------------------------

Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não vai poder exceder 30% do salário ou então o emprestimo será negado
R:Aula12ex001

Escreva um programa que leia um número inteiro qualquer e peça para usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
R:Aula12ex002

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
-O primeiro valor e Maior
-O segundo valor e Maior
-Não existe valor maior, os dois são iguais
R:Aula12ex003

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.
Seu programa deverá mostrar o tempo que falta ou que passou do prazo
R:Aula12ex004

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: Reprovado
-Média entre 5.0 e 6.9: Recuperação
-Média 7.0 ou superior: Aprovado
R:Aula12ex005

A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-Ate 9 anos: MIRIM
-Ate 14 anos: INFANTIL
-Ate 19 anos: JUNIOR
-Ate 20 anos: SÊNIOR
-Acima: MASTER
R:Aula12ex006

Refaça o Ultimo desafio da aula 10, acrescentando o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes
R:Aula12ex007

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso ideal
-25 ate 30: Sobrepeso
-30 ate 40: Obesidade
-Acima de 40: Obesidade mórbida
R:Aula12ex008

Elabore um programa que calcule o valor a ser pago por um produto considerando o seu pagamento preço normal e condição de pagamento:
-A vista dinheiro/cheque: 10% de desconto
-A vista no cartão: 5% de desconto
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
R:Aula12ex009

Crie um programa que faça o computador jogar Jokenpô com você
R:Aula12ex010


