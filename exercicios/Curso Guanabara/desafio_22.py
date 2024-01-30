#Desafio 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome_completo = input('Digite seu nome completo: ')

print("Nome completo com todas as letras maiúsculas:" + nome_completo.upper())
print("Nome completo com todas as letras minúsculas:" + nome_completo.lower())

quantidade_nome_todo = len(nome_completo.split())
print(f"Quantidade de letras ao todo: {quantidade_nome_todo} ")

primeiro_nome = len(nome_completo.split()[0])
print(f"Quantidade de letras do primeiro nome: {primeiro_nome}")
