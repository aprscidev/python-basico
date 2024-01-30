#Desafio 62 - Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.O programa encerra quando ele disser que quer mostrar 0 termos.

n = 1
print('PROGRESSÃO ARITMÉTICA')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

while not n == 11:
    progressao = termo + ((n - 1) * razao)
    n = n + 1
    print(progressao)

print('--FIM--')