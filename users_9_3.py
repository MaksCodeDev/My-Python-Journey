class User:
    """Сводка информации о пользователе"""
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age

    def describe_user(self):
        """Выводит информацию о пользователе"""
        print(f"\nПользователь {self.first_name} {self.last_name}.")
        print(f"Место проживания {self.location}")
        print(f"Возраст {self.age}")

    def greet_user(self):
        """Приветствие"""
        print(f"Добро пожаловать {self.first_name}")

user_1 = User('Виктор', 'баринов', 'Москва', 68)
user_2 = User('Макс', 'Лавров', 'Москва', 41)

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
