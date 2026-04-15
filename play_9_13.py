from random import randint

class Die:
    """Класс для предоставления игральной кости"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """выводит колво граней на кости от 6 до n"""
        print(randint(1, self.sides))

ten_sides_die = Die()
print('бросаем 10-гранный кубик')
for i in range(1, 11):
    ten_sides_die.roll_die()

twenty_sides_die = Die()
print('бросаем 20-гранный кубик')
for i in range(1, 21):
    twenty_sides_die.roll_die()