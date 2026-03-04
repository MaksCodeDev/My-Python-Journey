current_users = ['Denis', 'edik', 'jhon', 'maria', 'anjela']
new_users = ['denis', 'edik', 'ivan', 'petr', 'vika']

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Имя {new_user} занято")
    else:
        print(f"Имя {new_user} свободно")