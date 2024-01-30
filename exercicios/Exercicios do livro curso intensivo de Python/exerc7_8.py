#Exercicio 7.8
sandwich_orders = ['x-tudo', 'hamburguer', 'x-bacon', 'x-burguer'] 
finished_sandwiches = []

#Percorrendo a lista de pedidos com um laço e transferindo para a lista de finalizados
while sandwich_orders:
    prep_sandwich = sandwich_orders.pop()
    print("Preparando sanduíche: " + prep_sandwich)
    finished_sandwiches.append(prep_sandwich)

#Exibe todos os sanduíches prontos
print("\nSanduíches prontos:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
