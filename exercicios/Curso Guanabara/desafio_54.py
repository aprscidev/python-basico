#Desafio 54 - Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

contmaioridade = 0
contidade = 0

for p in range (1, 8):
    print(f'Pessoa {p} de 7.')
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - nascimento
    if idade < 21:
        contmaioridade = contmaioridade + 1
    else:
        contidade = contidade + 1

print(f'Quantidade de pessoas maiores de idade: {contmaioridade} ')
print(f'Quantidade de pessoas menores de idade: {contidade}')

