from city_11_1 import city_func

def test_city_func():
    """проверка содержится ли Santiago и Chile в функции"""
    formated_city = city_func('Santiago', 'Chile')
    assert formated_city == 'Santiago Chile'