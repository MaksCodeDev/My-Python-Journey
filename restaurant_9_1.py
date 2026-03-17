class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        """Инициализирует атрибуты названия и тип кухни."""
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        """Выводит информацию о ресторане."""
        print(f"Ресторан '{self.restaurant_name}' предлагает кухню: {self.cusine_type}")

    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт."""
        print(f"Ресторан '{self.restaurant_name}' сейчас открыт!")

restaurant = Restaurant('Панда', 'Тайская')
print(f"Название: {restaurant.restaurant_name}")
print(f"Тип кухни: {restaurant.cusine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()