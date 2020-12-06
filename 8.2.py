class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


while True:
    try:
        number_1 = int(input("Введите делимое: "))
        break
    except ValueError:
        print("Вводите число")
while True:
    try:
        number_2 = int(input("Введите делитель: "))
        break
    except ValueError:
        print("Вводите число")

try:
    if number_2 == 0:
        raise ZeroDivision("На ноль делить нельзя")
    else:
        print(number_1 / number_2)
except ZeroDivision:
    print("На ноль делить нельзя")
