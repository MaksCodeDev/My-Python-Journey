my_pizzas = ['peperoni', 'hawaiian', 'beshamel']
friend_pizzas = my_pizzas[:]
my_pizzas.append('margarita')
friend_pizzas.append('chese')
print(my_pizzas)
print(friend_pizzas)

print('\nМои любимы пиццы;')
for pizza in my_pizzas:
    print(f"-{pizza}")
print('Любимые пиццы моего друга;')
for pizza in friend_pizzas:
    print(f"-{pizza}")