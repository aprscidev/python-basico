#Exercício 9.5

class User():
    """Armazenamento de vários atributos relacionados a um perfil de usuário"""

    def __init__(self, first_name, last_name, age, matricula):
        """Inicializa os atributos"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.matricula = matricula
        self.login_attempts = 0

    def describe_user(self):
        """Resumo das informações do usuário"""
        print('Nome completo: ' + self.first_name.title() + ' ' + self.last_name.title() + ', ' + str(self.age) + ' anos e matrícula ' + str(self.matricula) + '.')

    def greet_user(self):
        """Saudação personalizada ao usuário"""
        print('Bem vindo(a) ' + self.first_name.title() + ' ' + self.last_name.title() + '!')

    def increment_login_attempts(self, increment):
        """Incrementa o valor de login_attempts em 1"""
        new_value = self.login_attempts + increment
        old_value = self.login_attempts
        self.login_attempts = new_value if increment > 0 else old_value
        print("Qtde de logins: " + str(self.login_attempts))

    def reset_login_attempts(self):
        """Reinicia o valor de login_attempts para 0"""
        self.login_attempts = 0

user1 = User('ana', 'paula', 27, 12345)
user2 = User('joao', 'silva', 48, 78452)
user3 = User('maria', 'sousa', 19, 85269)
user4 = User('jesus', 'castro', 70, 78125)

user1.describe_user()
user1.greet_user()

user1.reset_login_attempts()


