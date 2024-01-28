#Exercício 5 - Conceitos Básicos - Womakerscode

#Solicitando a distância da viagem
distancia = int(input('Digite a distância em quilômetros do destino: '))

#Calculando os tempos de acordo com o tipo de percurso
aviao = distancia / 600
carro = distancia / 100
onibus = distancia / 80

#Saídas
print(f'O percurso de {distancia} km é realizado em {aviao} horas em um avião.')
print(f'O percurso de {distancia} km é realizado em {carro} horas em um carro.')
print(f'O percurso de {distancia} km é realizado em {onibus} horas em um ônibus.')

#Finalizando
print('---')