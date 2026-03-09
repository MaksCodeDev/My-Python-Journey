def make_album(name_musician, album_musician):
    """Выводит исполнителя и альбом"""

    full = {'artist': name_musician, 'album': album_musician}

    return full
while True:
    print('Введите q для выхода')

    name = input('Имя исполнителя: ')
    if name.lower() == 'q':
        break
    
    album = input('Название альбома: ')
    if album.lower() == 'q':
        break

    result = make_album(name, album)
    print(result)