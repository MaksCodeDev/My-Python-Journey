class User:
    """Сводка информации о пользователе"""
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Выводит информацию о пользователе"""
        print(f"\nПользователь {self.first_name} {self.last_name}.")
        print(f"Место проживания {self.location}")
        print(f"Возраст {self.age}")

    def greet_user(self):
        """Приветствие"""
        print(f"\nДобро пожаловать {self.first_name}")
    
    def increment_login_attempts(self):
        """Счетчик"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Сброс"""
        self.login_attempts = 0

user_1 = User('Виктор', 'баринов', 'Москва', 68)
user_2 = User('Макс', 'Лавров', 'Москва', 41)

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user() 

print(f"Попыток входа у {user_1.first_name}: {user_1.login_attempts}")

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Попыток после ввода: {user_1.login_attempts}")

user_1.reset_login_attempts()
print(f"Попыток после сброса: {user_1.login_attempts}")