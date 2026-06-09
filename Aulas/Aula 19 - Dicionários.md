Tupla = ()
Listas = []
Dicionarios = {}

dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])

Adicionar elementos:
dados['sexo'] = 'M'

Apagar elementos:
del dados['idade']

Exemplo 1:

filme = { 'titulo': 'Star Wars',
	'ano': 1977,
	'diretor': 'George Lucas'	
}

print(filme.values())
R: 'Star Wars', '1977', 'George Lucas'

print(filme.keys())
R: 'titulo', 'ano', 'diretor'

print(filme.items())
R: TUDO

for k, v in filme.items():
	print(f'O {k} é {v}')
R: O titulo e Star Wars. O ano e 1977. O diretor e George Lucas

E possivel ter uma lista com varios dicionarios dentro:
![[Pasted image 20260604115952.png]]

`print(locadora[0]['ano'])` R: 1977
`print(locadora[2]['titulo']` R: Matriz

---

# DESAFIOS AULA 19 

Faça um programa que leia nome e média de um aluno. guardando também a situação em um dicionário. No final, mostra o conteúdo da estrutura na tela.
R: Aula19ex001
![[Pasted image 20260604124731.png]]

Crie um programa onda 4 jogadores joguem um dado a tenham resultados aleatórios. Guarda esses resultados em um dicionário. No final, coloque asse dicionário em ordem. sabendo que o vencedor tirou o maior número no dado.
R: Aula19ex002
![[Pasted image 20260604125057.png]]


Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastra-os (com idada) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule a acrescenta, além da idade, com quantos anos a pessoa vai se aposentar. (35 anos)
R: Aula19ex003
![[Pasted image 20260604125508.png]]


Crie um programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador a quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total da gols feitos durante o campeonato.
R: Aula19ex004
![[Pasted image 20260604125803.png]]


Crie um programa que leia nome, Sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário a todos os dicionários em uma lista. No final, mostra: 
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo. 
C) Uma lista com todas as mulheres. 
D) Uma lista com todas as pessoas com idade acima da média.
R: Aula19ex005
![[Pasted image 20260604130116.png]]


Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema da visualização da detalhes do aproveitamento de cada jogador.
R: Aula19ex005
![[Pasted image 20260604130328.png]]
![[Pasted image 20260604130347.png]]
