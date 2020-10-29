import time
from itertools import cycle

class TrafficLight:
    __TrafficLight_color = 0

    def __init__(self):
        self.running = 'Запуск !!!'

TrafficLight1 = TrafficLight()
print(TrafficLight1.running)
colors = [ f'red', 'yellow', 'green']
change = cycle(colors)
print(next(change))
time.sleep(7)
print(next(change))
time.sleep(2)
print(next(change))
time.sleep(10)

