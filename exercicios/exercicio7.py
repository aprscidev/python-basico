#Exercício 7 - Conceitos Básicos - Womakerscode

#Solicitando informações ao usuário
valor_hora = float(input('Digite o valor da hora trabalhada: '))
qtde_horas = int(input('Digite a quantidade de horas trabalhadas no mês: '))

#Realizando cálculo do salário
salario = valor_hora * qtde_horas

#Saída
print(f'O valor do salário considerando {qtde_horas} horas trabalhadas no mês ao valor de R${valor_hora:.2f} é de: R${salario:.2f}')

#Finalizando
print('---')

