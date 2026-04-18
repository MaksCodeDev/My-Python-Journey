from pathlib import Path

contents = input("Введите ваше имя сюда:")
path = Path('guest.txt')
path.write_text(contents)