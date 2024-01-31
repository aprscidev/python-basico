#Exercício 3 - Funções - Womakerscode

#Função para converter temperatura de graus celsius para graus Fahrenheit
def ctof(tempc):
    Fahrenheit = (tempc * 1.8) + 32
    print(f'A temperatura de {tempc} °C é igual a {Fahrenheit} °F.')

#Função para converter temperatura de graus Fahrenheit para graus Celsius
def ftoc(tempf):
    Celsius = (tempf - 32) / 1.8
    print(f'A temperatura de {tempf} °F é igual a {Celsius} °C.')

#Menu para usuário selecionar opção de conversão de temperatura
def menu():
    opcao = int(input('Digite a opção [1] °C para °F e [2] °F para °C: '))
    if opcao == 1:
        tempc = float(input('Digite a temperatura em °C (Graus Celsius): '))
        ctof(tempc)
    elif opcao == 2:
        tempf = float(input('Digite a temperatura em °F (Graus Fahrenheit): '))
        ftoc(tempf)

#Chamada da função de menu
menu()

#Finalização
print('---')