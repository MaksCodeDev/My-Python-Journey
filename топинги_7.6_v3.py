prompt = 'Введите топинг'
prompt += 'Введите quit для завершения заказа'
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Мы добавим в вашу пиццу {topping}")