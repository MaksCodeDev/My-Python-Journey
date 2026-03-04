slink = {
    "species": 'hamster',
    'owner': 'sebastian',
}

snowbol = {
    'species': 'cocatoo parrot',
    'owner': 'jontan',
}

turbo = {
    'species': 'turtle',
    'owner': 'olivia'
}
pets = [slink, snowbol, turbo]
for animal in pets:
    specials = f"Это {animal['species']} его хозяина зовут {animal['owner'].title()}"
    print(specials)