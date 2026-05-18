'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expressao = input('Digite uma expressão com parênteses: ')

pilha = []

for char in expressao:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(char)
            break


if len(pilha) == 0:
    print('Expressão válida: parênteses estão corretamente abertos e fechados.')
else:
    print('Expressão inválida: parênteses abertos sem correspondência.')
