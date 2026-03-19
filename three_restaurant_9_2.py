class Restaurant:
    """Модель ресторана"""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты названия и тип кухни."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Выводит информацию о ресторане."""
        print(f"Ресторан '{self.restaurant_name}' предлагает кухню: {self.cuisine_type}")

restaurant_1 = Restaurant('В гостях у Ашота', 'Дагестанская')
restaurant_2 = Restaurant('Claude Monet', 'Французская')
restaurant_3 = Restaurant('Pasta la basta', 'Итальянская')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()