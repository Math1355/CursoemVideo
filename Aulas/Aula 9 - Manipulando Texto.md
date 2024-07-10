Isso e uma cadeia de caracteres/string  <- 'Curso em Video Python'
Deve estar em '' ou "".

frase = 'Curso em Video Python'

Fatiamento: 

frase [9] -> resulta 'V'
frase [9:13] -> resulta 'Vide'
frase[9:21] -> resulta 'Video Python'
frase[9:21:2] -> resulta 'VdoPto' (Um salto de 2 em 2)
frase [:5] -> resulta 'Curso'
frase[15:] -> resulta 'Python'
frase[9::3] -> resulta 'VePh'

Análise:

len(frase) -> mostra o comprimento da cadeia de caracteres, resulta em 21 
frase.count('o') -> conte quantas vezes o 'o'  aparece na cadeia de caracteres, resulta em 3
frase.count('o', 0, 13) -> conte quantas vezes o 'o' do zero ate o 12, resulta 1
frase.find('deo') -> quantas vezes ele encontrou 'deo' na cadeia de caracteres, resulta posição 11
frase.find('Android') -> se for procurar um conjunto de caracteres que não aparece na string ele retorna o resultado -1
'Curso' in frase -> Vai resultar True

Transformação

frase.replace('Python', 'Android') -> Aonde tiver Python ele vai trocar por Android
frase.upper() -> Deixa os caracteres em maiusculo
frase.lower() -> Deixa os caracteres em minusculo
frase.capitalize() -> Deixa somente o primeiro caractere em maiusculo
frase.title() -> Ele deixa a primeira letra pos um espaço em maiusculo

Nova frase:
   Aprenda Python  .

frase.strip() -> remove espaços no começo e no final
frase.rstrip() -> remove espaços do lado direito somente
frase.lstrip() -> remove espaços do lado esquerdo somente

Divisão

Antiga frase : 'Curso em Video Python'

frase.split() -> vai dividir os espaços, assim cada palavra vai receber um novo indice
Exemplo Curso = 0,1,2,3,4 -> 0
				em = 0,1 -> 1
				Video = 0,1,2,3,4 -> 2
				Python = 0,1,2,3,4,5 -> 3
(da para usar o split para outras coisas tambem)

'-'.join(frase) -> Vai juntar todos os elementos e usar o separador '-'

OBS: O python e Case sensitive ele diferencia maiuscula de minuscula.

Desafios aula 9:
---------------------------------------------

Crie um programa que leia o nome completo de uma pessoa e mostre:
	O nome com todas as letras maiúsculas
	O nome com todas as letras minúsculas
	Quantas letras ao todo (sem considerar espaços)
	Quantas letras tem o primeiro nome
	R: Aula9ex001

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
	Ex: Digite um número: 1834
	unidade: 4
	dezenas: 3
	centenas: 8
	Milhar: 1
	R:Aula9ex002

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
	R: Aula9ex003

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
	R: Aula9ex004

Faça um programa que leia uma frase pelo teclado e mostre:
	Quantas vezes a letra "A" aparece.
	Em que posição ela aparece a primeira vez
	Em que posição ela aparece pela última vez
	R: Aula9ex005

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
	Ex: Ana maria de Souza
	primeiro = Ana
	último = Souza
	R: Aula9ex006
