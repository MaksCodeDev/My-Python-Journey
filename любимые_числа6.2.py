favorite_digits = {
    'elizabed': [7, 5],
    'edward': [1, 3],
    'erik': [1, 2]
}
for name, favdig in favorite_digits.items():
    print(f"Я {name.title()}, мое любимое число:")
    for fav in favdig:
        print(f" {fav}")