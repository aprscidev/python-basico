#Exercício 9 - Tomada de decisão - Womakerscode

#Inicializando variáveis que farão a contagem de números pares e ímpares
cont_pares = 0
cont_impares = 0

#Laço de repetição para solicitar os valores ao usuário
while True:
    num = int(input("Digite um número. Digite zero para sair do programa."))
    if num == 0:
        break
    elif num < 0:
        print('Valor negativo.')
    elif num > 0:
        if (num % 2 == 0):
            cont_pares = cont_pares + 1
        elif (num % 2 == 1):
            cont_impares = cont_impares + 1
   
#Saídas
print(f'Quantidade de números pares digitados: {cont_pares}')
print(f'Quantidade de números ímpares digitados: {cont_impares}')

#Finalizando
print('---')