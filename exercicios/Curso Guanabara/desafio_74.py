#Desafio 74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
#valor que estão na tupla

from random import randint

lista_random = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Listagem de números sorteados: {lista_random}')
print(f'Maior valor da lista: {max(lista_random)}')
print(f'Menor valor da lista: {min(lista_random)}')
