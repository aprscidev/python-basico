#Desafio 57 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente, até ter um valor correto.

validacao = ('M', 'F')

sexo = str(input('Digite o sexo da pessoa (M/F): ')).strip().upper()
while sexo not in validacao:
    sexo = str(input('Dados inválidos. Digite o sexo da pessoa (M/F): ')).strip().upper()

print(f'Sexo {sexo} registrado com sucesso.')

print('--FIM--')