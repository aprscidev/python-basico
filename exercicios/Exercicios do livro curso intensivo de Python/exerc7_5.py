#Exercicio 7.5
prompt = "\nDigite sua idade: "
prompt += "\nDigite '500' para finalizar o programa."

idade = 0
while idade != 500:
    idade = int(input(prompt))
    if idade < 3:
        print("Ingresso gratuito.")
    elif (idade >= 3) and (idade < 12):
        print("O ingresso custará 10 dólares.")
    elif (idade >= 12) and (idade != 500):
        print("O ingresso custará 15 dólares.")



