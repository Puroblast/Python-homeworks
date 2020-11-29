class Road:
    # Методы
    def __init__(self, length, width):
        self.__length = int(length)
        self.__width = int(width)
        self.calculate()

    def calculate(self):
        weight = round((self.__length * self.__width * 25 * 5) / 1000)
        print(f"Необходимая масса асфальта: {weight} т.")


Road(5000, 20)
