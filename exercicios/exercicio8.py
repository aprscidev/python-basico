#Exercício 8 - Conceitos Básicos - Womakerscode

#Solicitando qtde de horas de exercício físico por semana.
qtde_horas = int(input('Digite a quantidade de horas de exercício físico por semana: '))

#Realizando cálculos. Considerando que um mês é igual a 4 semanas e uma hora 60 minutos.
calorias_total = ((qtde_horas * 60) * 5) * 4

#Saída
print(f'A quantidade de calorias queimadas no mês é: {calorias_total:.2f} ')

