def make_car(manufacturer, model, **car_info):
    """Выводит описание машины"""
    car_info['brand'] = manufacturer
    car_info['marka'] = model
    return car_info

car = make_car('toyta', 'camry', color='black', tow_package=True )
print(car)