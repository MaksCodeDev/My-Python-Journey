responses = {}   # Это пустой словарь. Сюда мы будем записывать: Имя = Место.
polling_active = True  # Это наш "флаг". Пока он True (Вкл), опрос идет

while polling_active: # "Пока рубильник ВКЛ — делай следующее:"
    name = input('Как вас зовут? ')
    place = input('Где хочешь отдохнуть? ')
    # "Пока рубильник ВКЛ — делай следующее:"
    responses[name] = place

    repeat = input('Еще кто то хочет пройти опрос? да/нет ')
    if repeat.lower() == 'нет':  # Если ввели 'нет'
        polling_active = False  # Переключаем рубильник в ВЫКЛ

print("\n---РЕЗУЛЬТАТЫ ОПРОСА---")
for name, place in responses.items():
    print(f"{name.title()} мечтает поехать в {place.title()}")
