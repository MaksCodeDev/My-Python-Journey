def show_messages(messages):
    """Выводит сообщения"""
    for message in messages:
        print(message)




def send_messages(send, messages):
    """Выводит ответ"""

    while messages:
        send_mes = messages.pop(0)
        new_message = f"Great {send_mes}"
        send.append(new_message)

my_list = ['привет', 'я учу питон', 'у меня скоро экзамены', 'как дела']
new_mes = []

send_messages(new_mes, my_list)
show_messages(new_mes)