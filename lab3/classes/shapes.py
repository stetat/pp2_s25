class Shape:
    def __init__(self):
        self.area = 0
    
    def parea(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.area = length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def calculate(self):
        print(self.length * self.width)


test = Shape()
rec = Rectangle(10, 20)
test.parea()
rec.calculate()