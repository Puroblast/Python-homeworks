class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}
        self.my_list = [f"{name}", f"{surname}", position, self._income]


class Position(Worker):
    def get_full_name(self):
        return " ".join(self.my_list[:2])

    def get_total_income(self):
        return f"{int(self._income['wage'] + self._income['bonus'])}"


p = Position(1, 2, 3, 4, 5)
print(f"{p.get_full_name()} общий доход составляет: {p.get_total_income()}")
