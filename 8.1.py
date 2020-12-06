class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def unzip(cls):
        my_list = x.split("-")
        try:
            return [int(my_list[i]) for i in range(len(my_list))]
        except (ValueError, TypeError):
            print("Вводите ЧИСЛА в формате День-Месяц-Год")
            exit()
            """Поставил exit для того чтобы следующие части программы не запускались и не выдавали множество ошибок"""
    @staticmethod
    def validation():
        if my_data.unzip()[0] < 1 or my_data.unzip()[0] > 31:
            print("Ввёденный день неверен")
        if my_data.unzip()[1] < 1 or my_data.unzip()[1] > 12:
            print("Введенный месяц неверен")
        if my_data.unzip()[2] < 1 or my_data.unzip()[2] > 9999:
            print("Введенный год неверен")
        print(f"Введенное число: {my_data.unzip()[0]}\nВведенный месяц: {my_data.unzip()[1]}"
              f"\nВведенный год: {my_data.unzip()[2]}")


x = input("Введите дату в формате день-месяц-год: ")
my_data = Data(x)
my_data.unzip()
my_data.validation()
