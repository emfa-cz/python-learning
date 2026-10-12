from abc  import ABC, abstractmethod

class shape:
    @abstractmethod
    def area(self):
        return 3.14 * self.radius ** 2

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class pizza(circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


shapes = [circle(radius=4), square(side=5), triangle(base=6, height=7), pizza(topping="pepperoni", radius=15)]

for shape in shapes:
    print(f"{shape.area()}cm2")