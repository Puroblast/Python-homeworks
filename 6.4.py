class Car:
    def __init__(self, speed, color, name, is_police):
        self.my_list = [speed, color, name, is_police]

    def go(self):
        print("go go go")

    def stop(self):
        print("stop")

    def turn(self, direction):
        print(f"go {direction}")

    def show_speed(self):
        print(self.my_list[0])


class TownCar(Car):
    def show_speed(self):
        if self.my_list[0] > 60:
            print("Превышение скорости")
        else:
            print("Я еду отлично")


class SportCar(Car):
    def drift(self):
        print("vghhhhhh")


class PoliceCar(Car):
    def is_it(self):
        if self.my_list[3] == True:
            print("виу виу виу")


class WorkCar(Car):
    def show_speed(self):
        if self.my_list[0] > 40 and self.my_list[3] != True:
            print("Превышение скорости")
        elif self.my_list[3] == True:
            print("виу виу виу")
        else:
            print("Я еду отлично")


p = PoliceCar(59, 2, 3, 1)
p.is_it()

w = WorkCar(39, 2, 3, 0)
w.show_speed()

s = SportCar(100, 2, 3, 0)
s.drift()

t = TownCar(50, 1, 4, 0)
t.show_speed()

c = Car(50, 1, 2, 1)
c.go()
c.turn("right")
c.stop()
