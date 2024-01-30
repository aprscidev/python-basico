#Exercicio 7.10
responses = {}

#Flag para indicar que a enquete está ativa
polling_active = True
while polling_active:
    name = input("\nQual é seu nome? ")
    response = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")
    responses[name] = response
    resposta = input("Outra pessoa responderá à enquete? (sim/nao) ")
    if resposta == 'nao':
        polling_active = False

#Enquete concluída. Mostrando resultados.
print("\n--- Resultados da Enquete ---")
for name, response in responses.items():
    print(name + " gostaria de visitar " + response + ".")