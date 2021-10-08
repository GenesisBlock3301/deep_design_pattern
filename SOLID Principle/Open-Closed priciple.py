# one class perform one duty
import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius**2)


class Square:
    def __init__(self,lenght):
        self.lenght = lenght

    def area(self):
        return self.lenght**2


class AreaCalculator:
    def __init__(self,arr = []):
        self.arr = arr

    def sum(self):
        lis = []
        for i in self.arr:
            lis.append(i.area())
            # bad practice
            # # print(isinstance(i,Square))
            # if isinstance(i,Square):
            #     lis.append(i.lenght**2)
            # if isinstance(i,Circle):
            #     lis.append(math.pi*(i.radius**2))
        return lis

    def output(self):
        return self.sum()


shapes = AreaCalculator([Circle(2),Square(5),Square(6)])
print(shapes.sum())


