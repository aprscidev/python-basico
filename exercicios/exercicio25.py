#Exercício 5 - Funções - Womakerscode

#Função para calcular quantidade de vogais
def contvogais():
    frase = input('Digite uma frase para contagem de vogais: ').upper()
    qtdea = frase.count("A")
    qtdee = frase.count("E")
    qtdei = frase.count("I")
    qtdeo = frase.count("O")
    qtdeu = frase.count("U")
    total_vogais = qtdea + qtdee + qtdei + qtdeo + qtdeu
    print(f'A frase {frase} possui {total_vogais} vogais.')

#Chaando a função
contvogais()