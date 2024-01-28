#Exercício 2 - Conceitos Básicos - Womakerscode

#Importação da biblioteca para sempre considerar o ano atual

from datetime import date

#Solicitando ano de nascimento do usuário
ano_nascimento = int(input('Digite o ano do seu nascimento (AAAA): '))

#Cálculo da idade
idade = int(date.today().year - ano_nascimento)

#Saída
print(f'Sua idade, considerando o ano atual, é: {idade} anos.')

#Finalizando
print('---')

