#Desafio 26 - Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece na primeira vez.
#Em que posição ela aparece pela últim vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print(f"Quantidade de vezes que a letra A aparece: {frase.count('A')}")
print(f"A primeira letra A apareceu na posição: {frase.find('A')+1}")
print(f"A última letra A apareceu na posição: {frase.rfind('A')+1}")
