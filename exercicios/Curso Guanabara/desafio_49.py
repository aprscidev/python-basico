#Desafio 49 - Refaça o desafio 9 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para mostrar a sua tabuada: '))
for n in range (0, 10):
    tabuada = n * num
    print(f'{num} x {n} = {tabuada}')
print('--FIM--')