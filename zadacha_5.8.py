users = ['admin', 'maxim']
if users:
    for user in users:
        if user == 'admin':
            print("Здравствуйте admin! Хотите посмотреть отчет о состояние сервера?")
        else:
            print(f"Здраствуйте {user} спасибо что зарегистрировались на нашем сайте!")
else:
    print("Нам нужны пользователи")