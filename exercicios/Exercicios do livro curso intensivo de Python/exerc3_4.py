#Exercicio 3.4
convidados = ["Freedie", "Lady", "Justin"]
message = ", você está convidado para o jantar que acontecerá dia 25/07!"
print(convidados[0].title()+ message + "\n\t")
print(convidados[1].title()+ message + "\n\t")
print(convidados[2].title()+ message + "\n\t")
print(convidados[0].title()+ " não comparecerá ao jantar.\n\t")

#Exercicio 3.5
convidados[0] = "Suzana"
print(convidados[0].title()+ message + "\n\t")
print(convidados[1].title()+ message + "\n\t")
print(convidados[2].title()+ message + "\n\t")

#Exercicio 3.6
print("Uma mesa maior estará disponível para o jantar.\n\t")
convidados.insert(0, "Francisco") #inserindo nome no início da lista
convidados.insert(2, "Maria") #inserindo nome no meio da lista
convidados.append("Laura") #inserindo usando append no final da lista
print(convidados[0].title()+ message + "\n\t")
print(convidados[1].title()+ message + "\n\t")
print(convidados[2].title()+ message + "\n\t")
print(convidados[3].title()+ message + "\n\t")
print(convidados[4].title()+ message + "\n\t")
print(convidados[5].title()+ message + "\n\t")

#Exercicio 3.7
print("A mesa de jantar não chegará a tempo e teremos espaço apenas para 2 convidados. \n\t")

#utilizando pop para remover convidados da lista
print(convidados.pop(5)+", infelizmente não será possível continuar com o seu convite do jantar. \n\t")
print(convidados.pop(4)+", infelizmente não será possível continuar com o seu convite do jantar. \n\t")
print(convidados.pop(3)+", infelizmente não será possível continuar com o seu convite do jantar. \n\t")
print(convidados.pop(2)+", infelizmente não será possível continuar com o seu convite do jantar. \n\t")

#mensagem para as duas pessoas que continuam na lista
print(convidados[0].title()+ message + "\n\t")
print(convidados[1].title()+ message + "\n\t")

#Exercicio 3.9
qtde =  len(convidados)
print("Número de convidados definidos para o jantar: ")
print(qtde)


#removendo os dois últimos nomes da lista
del convidados[0]
del convidados[0]

print(convidados)

