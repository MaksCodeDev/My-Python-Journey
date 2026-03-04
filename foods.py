my_foods = ['pizza', 'falafel', 'carrot cace']
friend_foods = my_foods[:]

print('\nMy favorite foods are:')
print(my_foods)

print('\nMy friend`s favorite foods are:')
print(friend_foods)

my_foods.append('canoli')
friend_foods.append('ice cream')

print('\nMy favorite foods are:')
print(my_foods)

print('\nMy friend`s favorite foods are:')
print(friend_foods)
my_foods.append('chac-chac')

print(f"Первые три пункта в списке - это:{my_foods[:3]}")
print(f"Три пункта из середины списка:{my_foods[1:4]}") 
print(f"Последние три пункта в списке - это:{my_foods[2:5]}")
print(my_foods)
print(friend_foods)