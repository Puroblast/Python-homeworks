class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __floordiv__(self, other):
        if round(self.cell / other.cell) <= 0:
            return "Введите корректные данные"
        else:
            return round(self.cell / other.cell)

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return self.cell - other.cell
        else:
            return "Разность ячеек отрицательная"

    def __mul__(self, other):
        return self.cell * other.cell

    def make_order(self, raw):
        my_list = []
        for i in range(self.cell):
            if i % raw == 0 and i != 0:
                my_list.append("\n*")
            else:
                my_list.append("*")
        print("".join(my_list))


cell_1 = Cell(25)
cell_2 = Cell(500)
print(cell_1.__add__(cell_2))
print(cell_1.__floordiv__(cell_2))
print(cell_1.__mul__(cell_2))
print(cell_1.__sub__(cell_2))
cell_1.make_order(3)
