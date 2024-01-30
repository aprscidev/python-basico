#Exercício 5 - Tomada de decisão - Womakerscode

#Solicitando valores de comprimento ao usuário
lado1 = int(input('Digite o primeiro lado do triângulo: '))
lado2 = int(input('Digite o segundo lado do triângulo: '))
lado3 = int(input('Digite o terceiro lado do triângulo: '))

#Realizando verificações
if lado1 == lado2 and lado2 == lado3:
    print('Triângulo Equilátero!')
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print('Triângulo Escaleno!')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Triângulo Isósceles!')

#Finalizando
print('---')

