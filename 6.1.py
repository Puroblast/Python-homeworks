import turtle as t
import time


class TrafficLight:
    # Атрибуты
    __colour = ["red", "yellow", "green", "yellow"]
    seconds = [7, 2, 5, 2]

    # Методы
    def start(self):
        while True:
            for i in range(len(self.__colour)):
                t.color(self.__colour[i])
                t.begin_fill()
                t.circle(50)
                t.end_fill()
                time.sleep(self.seconds[i])


start_1 = TrafficLight()
start_1.start()
