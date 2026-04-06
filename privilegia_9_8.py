class User:
    """Сводка информации о пользователе"""
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0
        self.privelegia_guest = [
            'посещать сайт',
            'получать доступ к эксклюзивным возможностям с подпиской премиум'
        ]
        
    def show_privelegia(self):
        """выводит привелегии пользователя."""
        print(f"Привелегии посетителя {self.first_name}:")
        for privilegii in self.privelegia_guest:
            print(privilegii)

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

class Privileges:
    """класс для хранения привелегий."""
    def __init__(self):
        # переносим список сюда
        self.privileges = [
            'разрешено добавлять сообщения',
            'разрешено удалять пользователя',
            'разрешено банить пользователей'
        ]

    def show_privileges(self):
        """выводит привелегии админа."""
        
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """особый вид пользователя."""
    def __init__(self, first_name, last_name, location, age):
        super().__init__(first_name, last_name, location, age)
        self.privileges = Privileges()
    
user_1 = User('Виктор', 'баринов', 'Москва', 68)

user_1.describe_user()
user_1.greet_user()
user_1.show_privelegia()

print(f"Попыток входа у {user_1.first_name}: {user_1.login_attempts}")

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Попыток после ввода: {user_1.login_attempts}")

user_1.reset_login_attempts()
print(f"Попыток после сброса: {user_1.login_attempts}")

admin_max = Admin('Макс', 'Лавров', 'Франция', '25')
admin_max.describe_user()
admin_max.privileges.show_privileges()