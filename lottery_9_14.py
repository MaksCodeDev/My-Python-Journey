from random import choice

lottery = [0, 1, 3, 2, 77, 100, 222, 000, 67, 52, 'a', 'b', 'c', 'd', 'e']

win = []

while len(win) < 4:
    pulled_item = choice(lottery)

    if pulled_item not in win:
        win.append(pulled_item)

print(f"Дюбой биле содержащий эти 4 символа побеждает: {win}")