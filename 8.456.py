class Storage:
    def get_item(self):
        global my_dict
        global item
        item = input(
            "Введите что вы хотите добавить на склад 1 - принтер 2 - сканер 3 - ксерокс, 10 - если хотите выйти: ")
        if item.isdigit() is False:
            print("Вводите Числа 1 - принтер 2 - сканер 3 - ксерокс")
            return None
        if item == '1':
            try:
                quant = int(input("Какое количество вы хотели бы внести на склад? : "))
                if quant < 0:
                    print("Воздух не добавляем")
                else:
                    my_dict["Принтер"] = quant + my_dict.get("Принтер")
            except ValueError:
                print("Вводите число")
        elif item == '2':
            try:
                quant = int(input("Какое количество вы хотели бы внести на склад? : "))
                if quant < 0:
                    print("Воздух не добавляем")
                else:
                    my_dict["Сканер"] = quant + my_dict.get("Сканер")
            except ValueError:
                print("Вводите число")
        elif item == '3':
            try:
                quant = int(input("Какое количество вы хотели бы внести на склад? : "))
                if quant < 0:
                    print("Воздух не добавляем")
                else:
                    my_dict["Ксерокс"] = quant + my_dict.get("Ксерокс")
            except ValueError:
                print("Вводите число")
        elif item != "10":
            print("Вводите Число 1 - принтер 2 - сканер 3 - ксерокс, 10 - если хотите выйти ")
        print(my_dict)

    def take_item(self):
        global my_dict
        global item
        item = input(
            "Введите что вы хотите забрать из склада 1 - принтер 2 - сканер 3 - ксерокс, 10 - если хотите выйти: ")
        if item.isdigit() is False:
            print("Вводите Числа 1 - принтер 2 - сканер 3 - ксерокс")
            return None
        if item == '1':
            try:
                quant = int(input(
                    f"Какое количество забрать со склада?, количество на складе = {my_dict.get('Принтер')} : "))
                if quant > my_dict.get("Принтер"):
                    print("У нас столько нет")
                elif quant < 0:
                    print("Воздух не добавляем")
                else:
                    my_dict["Принтер"] = my_dict.get("Принтер") - quant
            except ValueError:
                print("Вводите число")
        elif item == '2':
            try:
                quant = int(input(
                    f"Какое количество забрать со склада?, количество на складе = {my_dict.get('Сканер')} : "))
                if quant > my_dict.get("Сканер"):
                    print("У нас столько нет")
                elif quant < 0:
                    print("Воздух не добавляем")
                else:
                    my_dict["Сканер"] = my_dict.get("Сканер") - quant
            except ValueError:
                print("Вводите число")
        elif item == '3':
            try:
                quant = int(input(
                    f"Какое количество забрать со склада?, количество на складе = {my_dict.get('Ксерокс')} : "))
                if quant > my_dict.get("Ксерокс"):
                    print("У нас столько нет")
                elif quant < 0:
                    print("Воздух не добавляем")
                else:
                    my_dict["Ксерокс"] = my_dict.get("Ксерокс") - quant
            except ValueError:
                print("Вводите число")
        elif item != "10":
            print("Вводите Число 1 - принтер 2 - сканер 3 - ксерокс, 10 - если хотите выйти ")
        print(my_dict)


class Equipment:
    def __init__(self, name, wide, length):
        self.wide = wide
        self.length = length
        self.name = name


class Printer(Equipment):
    def __init__(self, name, wide, length, technology):
        super().__init__(name, wide, length)
        self.tech = technology

    def __str__(self):
        return f"Принтер {self.name} ширина {self.wide} длина {self.length} с технологией печати {self.tech}"


class Scanner(Equipment):
    def __init__(self, name, wide, length, quality):
        super().__init__(name, wide, length)
        self.qual = quality

    def __str__(self):
        return f"Сканер {self.name} ширина {self.wide} длина {self.length} качество сканирования {self.qual}"


class Xerox(Equipment):
    def __init__(self, name, wide, length, speed):
        super().__init__(name, wide, length)
        self.speed = speed

    def __str__(self):
        return f"Ксерокс {self.name} ширина {self.wide} длина {self.length} скорость сканирования {self.speed}"


my_dict = {"Ксерокс": 0, "Принтер": 0, "Сканер": 0}
p = Printer("Xls456", 45, 50, "Laser")
s = Scanner("KKK454", 76, 33, "1080p")
x = Xerox("LKJ8909", 50, 50, "fast")
while True:
    Storage().get_item()
    if item == "10":
        break
while True:
    Storage().take_item()
    if item == "10":
        break
