#Exercicio 8.4

def make_shirt(tamanho, mensagem = 'Eu amo Python'):
    print("Tamanho da camisa: " + tamanho)
    print("Texto da camisa: " + mensagem)

make_shirt('grande')
make_shirt('media')
make_shirt('pequena', mensagem = 'Eu sou o Batman!')