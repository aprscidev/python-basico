#Desafio 38 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem.
#O primeiro valor maior, o segundo valor maior, não existe valor maior, os dois são iguais.

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

if num1 > num2:
    print(f'Primeiro maior valor: {num1}.')
    print(f'Segundo maior valor: {num2}')
elif num1 < num2:
    print(f'Primeiro maior valor: {num2}')
    print(f'Segundo maior valor: {num1}')
elif num1 == num2:
    print('Não existe valor maior, os dois são IGUAIS.')
print('--FIM--')