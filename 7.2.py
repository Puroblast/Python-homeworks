from abc import abstractmethod


class Cloth:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @abstractmethod
    def formula(self):
        pass


class Coat(Cloth):
    @property
    def formula(self):
        total = (self.v / 6.5 + 0.5)
        return total


class Costume(Cloth):
    @property
    def formula(self):
        total = (2 * self.h + 0.3)
        return total


c = Coat(5, 2)
p = Costume(5, 2)
print(f"Общий расход ткани составляет: {round(c.formula + p.formula, 2)}")
