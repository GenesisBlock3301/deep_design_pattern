class Shape:
    def draw(self):
        print("Drawing shape")

class Rectangle(Shape):
    def draw(self):
        print("Draw ractangle")


shape = Shape()
shape = Rectangle()
shape.draw()