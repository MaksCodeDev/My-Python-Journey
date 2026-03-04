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