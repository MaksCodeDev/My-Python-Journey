from random import choice

lottery = [0, 1, 3, 2, 77, 100, 222, 000, 67, 52, 'a', 'b', 'c', 'd', 'e']
my_ticket = ['a', 'd', 52, 'b']
win = []
iterations = 0

while win != my_ticket:
    iterations += 1
    win = []
    while len(win) < 4:
        pulled_item = choice(lottery)
        if pulled_item not in win:
            win.append(pulled_item)

print(f"Победа! Понадобилось попыток: {iterations}")
print(f"Выиграшная комбинация: {win}")