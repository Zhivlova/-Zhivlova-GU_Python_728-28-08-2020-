class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __add__(self, other):
        return f'сумма ячеек двух клеток: {self.cells + other.cells}'

    def __sub__(self, other):
        subtraction = self.cells - other.cells
        return f'разность количества ячеек: {subtraction}' if subtraction > 0 else 'Клетка исчезла'

    def __truediv__(self, other):
        return self.cells // other.cells

    def __mul__(self, other):
        return self.cells * other.cells

    def make_order(self, row):
        result = ''
        for i in range(int(self.cells / row)):
            result += '*' * row + '\n'
        result += '*' * (self.cells % row) + '\n'
        return result

cell = Cell(36)
cell_2 = Cell(6)
print(cell+cell_2)
print(cell-cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))
