def info(name, surname, date, city, mail, phone):
    print(f"Имя:{name},Фамилия:{surname},Год рождения:{date},Город:{city},Почта:{mail},Телефон:{phone}")


info(name=input("Введите имя: "), surname=input("Введите фамилию: "), date=input("Введите год рождения: "),
     city=input("Введите город проживания: "), mail=input("Введите вашу почту: "),
     phone=input("Введите номер телефона: "))
