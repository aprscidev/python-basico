#Desafio 79 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos, em ordem crescente.

valores = []
while True:
    valor = int(input('Digite um número: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Número já foi digitado. Digite um novo valor: ')

    opcao = str(input('Deseja digitar um novo valor? (S/N)'))
    if opcao in 'Nn':
        break

valores.sort()
print(f'Você adicionou os números {valores}')

