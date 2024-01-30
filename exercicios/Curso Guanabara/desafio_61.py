#Desafio 61 - Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura while

n = 1
print('PROGRESSÃO ARITMÉTICA')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

while not n == 11:
    progressao = termo + ((n - 1) * razao)
    n = n + 1
    print(progressao)

print('--FIM--')