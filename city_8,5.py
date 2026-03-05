def describe_city(city, country='россии'):
    """Выводит информацию о городе и стране"""
    print(f"{city.title()} находится в {country.title()}")

describe_city('москва')

describe_city('питер')

describe_city('рейкьявик', 'исландия')