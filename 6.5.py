class Stationery:
    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером")


Pen().draw()
Pencil().draw()
Handle().draw()
