#Exercício 6 - Conceitos Básicos - Womakerscode

#Solicitando peso e altura ao usuário
peso = int(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))

#Realizando cálculo do IMC
imc = peso / (altura * altura)

#Saída
print(f'O IMC considerando peso de {peso} kg e altura de {altura} metros é de: {imc:.2f}')

#Finalizando
print('---')

