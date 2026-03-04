kub = []
for num in range(1, 10):
    kub.append(num**3)
print(kub)
#ИЛИ МОЖНО СОЗДАТЬ ГЕНЕРАТОР В СПИСКЕ->
kub = [value**3 for value in range(1, 11)]
print(kub)