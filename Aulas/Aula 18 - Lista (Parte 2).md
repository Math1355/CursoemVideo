pessoas = list()
dados = list('Pedro', 25)
dados = list('Maria', 19)
dados = list('Joao', 32)
pessoas.append(dados[:]) <- copia dos dados

![[Pasted image 20260525224648.png]]

`pessoas = [['Pedro', 25], ['Maria', 19], ['Joao', 32]]`

`print(pessoas[0][0])`
Resultado: Pedro

`print(pessoas[1][1])`
Resultado: 19

`print(pessoas[2][0])`
Resultado: João

`print(pessoas[1])`
Resultado: `['Maria', 19]`

---
# DESAFIOS AULA 17

Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves.
Exemplo: ![[Pasted image 20260525230731.png]]
R:


Crie um programa onde o usuário possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente
Exemplo: ![[Pasted image 20260525230957.png]]
R:


Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |     |     |

No final, mostre a matriz na tela, com formtação correta.
Exemplo: ![[Pasted image 20260525231256.png]]
R:


Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A Soma dos valores da terceira coluna.
C) O maior valor da segunda linha
Exemplo: ![[Pasted image 20260525231504.png]]
R:


Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
Exemplo: ![[Pasted image 20260525231814.png]]
R:


Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
Exemplo: ![[Pasted image 20260525232130.png]]
![[Pasted image 20260525232149.png]]
R: