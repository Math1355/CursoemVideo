"""
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para 
cada palavra, quais são as suas vogais, exemplo:
"""

palavras = ("aprender", "programar", "linguagem", "python"
            , "curso", "gratis", "estudar", "praticar"
            , "trabalhar", "mercado", "programador", "futuro")

vogais = ["a", "e", "i", "o", "u"]

for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos ", end= "")

    for letra in palavra:
        if letra in vogais:
            print(letra, end=" ")