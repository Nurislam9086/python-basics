hours = int(input("Введите вряма:"))
if 6 <= hours <= 11:
    print("Доброе утро!")
elif 12 <= hours <= 17:
    print("Добрый день!")
elif 18 <= hours <=22:
    print("Добрый вечер!")
else:
    print("Спокойно ночи!")