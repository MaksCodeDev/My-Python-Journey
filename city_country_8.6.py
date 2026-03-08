def city_country(city, country):
    """Выводит страну - город"""
    full = f"{country}, {city}"
    return full.title()

pair1 = city_country('russia', 'ekaterinburg')
pair2 = city_country('japan', 'tokyo')
pair3 = city_country('france', 'paris')

print(pair1)
print(pair2)
print(pair3)