favorite_places = {
    'jonh': ['moscow', 'spb', 'ekb'],
    'liza': ['jenev', 'tokyo'],
    'stas': ['canada']
}
for name, places in favorite_places.items():
    print(f"Я {name.title()}, и мне нравится:")
    for place in places:
        print(place.title())
    