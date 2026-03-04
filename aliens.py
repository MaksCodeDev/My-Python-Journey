alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = []
# создание 30 зеленых пришельцев
for alien_numbers in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'clow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien ['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15 
        
# вывод данных о первых пяти пришельцах
for alien in aliens[:5]:
    print(alien)
print('...')

# вывод количества  созданных пришельцев
print(f"Total number of aliens: {len(aliens)}")