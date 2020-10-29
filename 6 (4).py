class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return self.name + 'поехала'

    def stop(self):
        return self.name + 'остановилась'

    def turn(self, direction):
        return self.name + 'повернула' + direction

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(self.speed + 'Скорость превышена')
        else:
            print(self.speed)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(self.speed + 'Скорость превышена')
        else:
            print(self.speed)

class SportCar(Car):
    pass
class PoliceCar(Car):
    pass

town = TownCar(78, 'grey', 'Volkswagen', False)
print(town.go(), town.show_speed(), town.turn('налево'), town.stop())

sport = SportCar(180, 'black', 'Mercedes', False)
print(sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar(47, 'white', 'Peugeot', False)
print(work.go(), work.show_speed(), work.turn('прямо'), work.stop())

police = PoliceCar (100, 'Ford', 'yellow', True)
print(police.go(), police.show_speed(), police.stop())