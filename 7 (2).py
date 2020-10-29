from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

@abstractmethod
def expenses(self):
    return f' Для пошива пальто нужно: {self} ткани '
    pass

class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def expenses_coat(self, v):
        return f'Для пошива пальто нужно: (v / 6.5 + 0.5 : .2f ) ткани'

class Costume(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def expenses_costume(self, h):
        return f'Для пошива костюма нужно: (2 * h.param + 0.3 : .2f) ткани '

coat = Coat(500)
costume = Costume(65)
print(coat.expenses_coat())
print(costume.expenses_costume())
