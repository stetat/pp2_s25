class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"X: {self.x}\nY: {self.y}")

    def move(self, nx, ny):
        self.x = nx
        self.y = ny

    def dist(self, x1, y1):
        return round(((x1-self.x)**2 + (y1-self.y)**2)**0.5, 3)


p1 = Point(1, 1)
p2 = Point(3, 3)

print(p2.dist(p1.x, p1.y))
p1.move(2, 2)
p1.show()