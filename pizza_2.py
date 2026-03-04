# сохранение информации о заказанной пицце
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# описание заказа
print(f"Вы заказали {pizza['crust']}-crust pizza "
      "со следующими добавками:")
# описание заказа
for topping in pizza['toppings']:
    print(f"\t{topping}")
