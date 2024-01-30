#Desafio 42 - Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if reta1 == reta2 and reta1 == reta3:
        print('TRIÂNGULO EQUILÁTERO.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('TRIÂNGULO ISÓSCELES.')
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print('TRIÂNGULO ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
print('--FIM--')