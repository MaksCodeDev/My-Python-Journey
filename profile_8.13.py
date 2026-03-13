def build_profile(first, last, **user_info):
    """Создает словарь, содержащий информацию о пользователе"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('maikl', 'jordan',
                             hobby='golf',
                             city='Florida',
                             age=63)
for user in user_profile:
    print(user_profile) 
