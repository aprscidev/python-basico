#Desafio 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o nome completo: ')).strip()
if "Silva" in nome.title():
    print('Este nome possui SILVA!')
else:
    print('Este nome não possui SILVA!')