#Desafio 72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
#(entre 0 e 20) e mostrá-lo por extenso

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quartro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: '))
while (num > 20):
    num = int(input('Valor inválido. Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break

print(f'{num} - {extenso[num]}')
print('--FIM--')