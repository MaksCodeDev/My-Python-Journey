alien_color = input('Какой цвет?')
price = 5
price1 = 10
price2 = 15
price3 = 20

if 'green' in alien_color:
    print(f"Вы получили {price} единиц опыта")
elif 'yelow' in alien_color:
    print(f"Вы получили {price1} единиц опыта")
elif 'red' in alien_color:
    print(f"Вы получили {price3} единиц опыта")
else:
    print(f"Вы получили {price2} единиц опыта")
