#Desafio 65 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, moste a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = int(input('Digite um valor: '))
soma_numeros = 0
maior_num = 0
menor_num = n
finalizar = True
contador = 0

while finalizar:
    soma_numeros = soma_numeros + n
    contador = contador + 1
    if n > maior_num:
        maior_num = n
    elif n < menor_num:
        menor_num = n
    opcao = str(input('Gostaria de continuar a digitar valores? [S/N]')).upper()
    if opcao == 'N':
        finalizar = False
    elif opcao == 'S':
        n = int(input('Digite um valor: '))
media = soma_numeros / contador
print(f'Média entre os números digitados: {media} ')
print(f'Maior número digitado: {maior_num}')
print(f'Menor número digitado: {menor_num}')