persona = {
    'first_name': 'jonh', 
    'last_name': 'parker',
    "age": 25,
    'city': 'california'
}

persona2 = {
    'first_name': 'brad',
    'last_name': 'pitt',
    'age': 62,
    'city': 'new york',
}

persona3 = {
    'first_name': 'sem',
    'last_name': 'melow',
    'age': '47',
    'city': 'tayvan',
}

people = [persona, persona2, persona3]

for pers in people:
    full_names = f"\n{pers['first_name'].title()} {pers['last_name'].title()}"
    age = pers['age']
    city = pers['city']
    print(f"{full_names} живет в городе {city}. Возраст {age}")