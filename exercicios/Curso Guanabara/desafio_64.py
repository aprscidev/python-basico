#Desafio 64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostra quantos números foram digitados e qual foi a sona entre eles (desconsiderando o flag).

n = int(input('Digite um valor. Digite [999] para encerrar o programa. '))
qtde_numeros = 0
soma_numeros = 0

while not n == 999:
    qtde_numeros = qtde_numeros + 1
    soma_numeros = soma_numeros + n
    n = int(input('Digite um valor. Digite [999] para encerrar o programa.'))
print(f'Quantidade de números digitados: {qtde_numeros}')
print(f'Soma dos numeros digitados: {soma_numeros}')
