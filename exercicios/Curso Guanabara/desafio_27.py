#Desafio 27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input('Digite o nome completo: ')).strip().title()

print(f'Seu primeiro nome é: {nome_completo.split()[0]}')
print(f'Seu último nome é: {nome_completo.split()[-1]}')
