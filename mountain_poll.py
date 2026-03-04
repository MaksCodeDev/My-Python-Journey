# Создание пустого словаря для хранения информации о пользователе опроса
responses = {}
# Установка флага продолжение опроса
polling_active = True

while polling_active:
    # Запрос имени и ответ пользователя
    name = input("\nКак вас зовут? ")
    response = input("На какую гору вы бы хотели подняться? ")
    # Ответ сохраняется в словаре
    responses[name] = response

    # Проверка предложения опроса.
    repeat = input("Вы бы хотели, чтобы ответил другой человек? (да/нет) ")
    if repeat == 'нет':
        polling_active = False
# Опрос завершен, вывести результаты.
print("\n--- Результаты Опроса ---")
for name, response in responses.items():
    print(f"{name} хотел бы подняться на гору: {response}")