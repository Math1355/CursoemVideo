Condições simples e Compostas

Quase todos os programas precisam de condições

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
	senão 
		carro.siga() <- bloco falso
		carro.esquerda()
		carro.siga()
		carro.esquerda()
		carro.siga()
carro.para()

Condição em python:

if carro.esquerda():
	bloco True
else:
	bloco False	

Exemplo:
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
	print('carro novo')
else:
	print('carro velho')
print('--FIM--')

Condição simplificada:
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo'if tempo <= 3 else 'carro velho')
print('--FIM--')

DESAFIOS AULA 10
--------------------------------------

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
	OBS: O programa deverá escrever na tela se o usuário venceu ou perdeu
	R: Aula10ex001

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
	R: Aula10ex002

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
	R: Aula10ex003

Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200Km e R$0,45 para viagens mais longas.
	R: Aula10ex004

Faça um programa que leia um ano qualquer e mostre se ele e BISSEXTO.
	R: Aula10ex005

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
	R: Aula10ex006

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento e de 15%.
	R: Aula10ex007

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não forma um triângulo.
	R: Aula10ex008

