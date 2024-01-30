#Exercicio 7.4
prompt = "\nDigite o nome do ingrediente da pizza: "
prompt += "\nDigite 'quit' para finalizar o programa."

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


