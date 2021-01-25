class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'общая площадь ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coats(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'расход площади ткани на пальто {self.square_c}'


class Jac(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'расход площади ткани на костюм {self.square_j}'

coat = Coats(10, 4)
jacket = Jac(20, 3)
print(coat)
print(coat.get_sq_full)
print(coat.get_square_c())
print(jacket)
print(jacket.get_sq_full)
print(jacket.get_square_j())