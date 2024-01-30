#Desafio 66 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

contador = 0
soma = 0
n = 0

while True:
    n = int(input('DIgite um número. Digite [999] para parar o programa.'))
    if n == 999:
        break
    else:
        contador = contador + 1
        soma = soma + n
print(f'Quantidade de números digitados: {contador}')
print(f'Soma dos números digitados: {soma}')