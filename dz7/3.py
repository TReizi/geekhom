class Сage:
    def __init__(self, dimension):
        self.dimension = int(dimension)

    def __str__(self):
        return f'Результат {self.dimension * "#"}'

    def __add__(self, other):
        return Сage(self.dimension + other.dimension)

    def __sub__(self, other):
        return self.dimension - other.dimension if (self.dimension - other.dimension) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Сage(int(self.dimension * other.dimension))

    def __truediv__(self, other):
        return Сage(round(self.dimension // other.dimension))

    def make_order(self, dimension_in_row):
        row = ''
        for i in range(int(self.dimension/ dimension_in_row)):
            row += f'{"#" * dimension_in_row} \\n'
        row += f'{"#" * (self.dimension % dimension_in_row)}'
        return row

сage1 = Сage(33)
сage2 = Сage(9)
print(сage1)
print(сage1 + сage2)
print(сage2 - сage1)
print(сage2.make_order(5))
print(сage1.make_order(10))
print(сage1 / сage2)