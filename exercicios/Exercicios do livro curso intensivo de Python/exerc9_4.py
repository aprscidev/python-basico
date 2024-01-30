#Exercicio 9.4

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos restaurant_name e cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Exibe as informações de restaurant_name e cuisine_type"""
        print(self.restaurant_name.title() + " é o nome do restaurante.")
        print(self.cuisine_type.title() + " é o tipo de culinária do restaurante.")

    def open_restaurant(self):
        """Exibe uma mensagem informando que o restaurante está aberto."""
        print('O restaurante está aberto.')

    def read_clients(self):
        """Exibe uma frase que mostra a quantidade de clientes atendidos"""
        print("Foram atendidos " + str(self.number_served) + " clientes hoje.")

    def set_number_served(self, clientes):
        """Define o número de clientes atendidos"""
        self.number_served = clientes

restaurant = Restaurant('Dona Marguerita', 'pizzaria')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(21)
restaurant.read_clients()