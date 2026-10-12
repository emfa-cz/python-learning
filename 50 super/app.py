class shape:
    def __init__(self, colour, isFilled):
        self.colour = colour
        self.isFilled = isFilled


class circle(shape):
    def __init__(self, colour, isFilled, radius):
        super().__init__(colour, isFilled)
        self.radius = radius

class square(shape):
        def __init__(self, colour, isFilled, width):
        super().__init__(colour, isFilled)
        self.width = width

class triangle(shape):
        def __init__(self, colour, filled, width, height):
        super().__init__(colour, isFilled)
        self.width = width
        self.height = height

cicle = circle(color="blue", isFilled=True, radius=5)

print(circle.colour)
print(circle.isFilled)