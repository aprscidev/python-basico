# Exercício 9.2
import self


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos restaurant_name e cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Exibe as informações de restaurant_name e cuisine_type"""
        print("Restaurante: " + self.restaurant_name.title())
        print("Tipo: " + self.cuisine_type.title())

    def open_restaurant(self):
        """Exibe uma mensagem informando que o restaurante está aberto."""
        print('O restaurante' + self.restaurant_name + ' está aberto.')


restaurant = Restaurant('Dona Marguerita', 'pizzaria')
restaurant2 = Restaurant('Nino', 'Pizzaria')
restaurant3 = Restaurant('Yukai', 'comida japonesa')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
