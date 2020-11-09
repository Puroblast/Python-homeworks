time = int(input("Введите время в секундах "))

hours = time // 3600
if hours >= 24:
    days = hours // 24
    hours = (time - (days * 24 * 3600)) // 3600
    minutes = (time - (days * 24 * 3600) - (hours * 3600)) // 60
    seconds = time - (days * 24 * 3600) - (hours * 3600) - (minutes * 60)
    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
else:
    minutes = (time - (hours * 3600)) // 60
    seconds = time - (hours * 3600 + minutes * 60)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
##Пытался отформатировать через %H:%M:%S , почему-то не вышло, выдавало Invalid format
