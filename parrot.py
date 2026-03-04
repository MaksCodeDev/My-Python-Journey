prompt = "\nСкажи мне что-нибудь, и я повторю это тебе:"
prompt += "\nВведите 'quit' для завершения программы. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)