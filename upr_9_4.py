class Restaurant:
    """Модель ресторана"""
    def __init__(self, restaurant_name, cusine_type):
        """Инициализирует атрибуты названия и тип кухни."""
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Выводит информацию о ресторане."""
        print(f"Ресторан '{self.restaurant_name}' предлагает кухню: {self.cusine_type}")

    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт."""
        print(f"Ресторан '{self.restaurant_name}' сейчас открыт!")

    def set_number_served(self, number):
        """Устаналивает заданное количество обслуженных гостей."""
        self.number_served = number 

    def increment_number_served(self, guests):
        """Добавляет число к текущем количеству гостей."""
        self.number_served += guests

restaurant = Restaurant('Панда', 'Тайская')
print(f"Обслужено гостей: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Обслужено после банкета {restaurant.number_served}")

restaurant.increment_number_served(25)
print(f"Итого после банкета {restaurant.number_served}")

print(f"Название: {restaurant.restaurant_name}")
print(f"Тип кухни: {restaurant.cusine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()