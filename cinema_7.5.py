prompt = "Введите возраст для определения стоимости цены билета (либо 'quit' для выхода) "
while True:
    age = input(prompt)
    if age == 'quit':
        print('Досвидания')
        break

    age = int(age)
    if age < 3:
        print("Вам вход бесплатен\n")

    elif age <= 12:
        print("Стоимость вашего билета 10$\n")

    elif age > 12:
        print("Стоимость вашего билета 15$\n")