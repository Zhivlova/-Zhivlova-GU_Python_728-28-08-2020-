import random
import numpy

class Ticket:

    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        return {}.format(self.numbers)

list1 =Ticket(numpy.random.randint(1, 90, size=(3, 5)))

class Player(Ticket):
    pass
print(f'------ Ваша карточка ----- \n{list1.numbers}')
barrel = random.randint(1, 90)
print(f'Новый бочонок :  {barrel}')
print('Зачеркнуть цифру? (y/n) ')

class Computer (Ticket):

    def __init__(self, numbers2):
        self.numbers2 = numbers2

    def __str__(self):
        return {}.format(self.numbers)

list2 = Computer(numpy.random.randint(1, 90, size=(3, 5)))
print(f'-- Карточка компьютера --- \n{list2.numbers2}')










