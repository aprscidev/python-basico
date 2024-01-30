#Exercício 9.3

class User():
    """Armazenamento de vários atributos relacionados a um perfil de usuário"""
    def __init__(self, first_name, last_name, age, matricula):
        """Inicializa os atributos"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.matricula = matricula

    def describe_user(self):
        """Resumo das informações do usuário"""
        print('Nome completo: ' + self.first_name.title() + ' ' + self.last_name.title() + ', ' + str(self.age) + ' anos e matrícula ' + str(self.matricula) + '.')

    def greet_user(self):
        """Saudação personalizada ao usuário"""
        print('Bem vindo(a) ' + self.first_name.title() + ' ' + self.last_name.title() + '!')

user1 = User('ana', 'paula', 27, 12345)
user2 = User('joao', 'silva', 48, 78452)
user3 = User('maria', 'sousa', 19, 85269)
user4 = User('jesus', 'castro', 70, 78125)

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user4.describe_user()
user4.greet_user()
