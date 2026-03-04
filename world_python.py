first_name = "maxon"
last_name = "lovelace"
full_name = f"hello, {first_name} {last_name}" # f для обьеденения нескольких переменных в одной
print(full_name)
message = f'{full_name}' # В F строку можнодаже засунуть переменную в которой итог переменной из нескольких переменных
print(message.title())



print("python")
print("\tpython") # \t для табуляции


print("languages:\npython\nC\nJavascript") #/n для разрыва строк

print("languages:\n\tpython\n\tC++\n\tJavascript") # \n  \t можно комбинировать

favorite_language = "python "
favorite_language.rstrip # для удаления пробелов в переменных с строковым типом данных
print(full_name)

languages = ' pthon '
#languages.ristrip()


nostrach_url = "https://nostrach.com"
nostrach_url.removeprefix('https://')
print(nostrach_url.removeprefix('https://'))   
