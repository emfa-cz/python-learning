class rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:1f}cm"

    @property
    def height(self):
        return f"self._height"

    @width.setter
    def width(self, width):
        if newWidth > 0:
            self._width = newWidth
        else:
            print("width must be greater than 0")

    @height.setter
    def height(self, width):
        if newHeight > 0:
            self.height = newHeight
        else:
            print("height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("deleted")

    @height.deleter
    def height(self):
        del self._height
        print("deleted")

    

rectange = rectangle(3, 4)
rectangle.width = 5
rectangle.height = 2

print(rectangle._width)
print(rectangle._height)