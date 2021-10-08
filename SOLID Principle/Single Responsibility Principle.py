# one class perform one duty


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def val(self):
        return self.radius


class Square:
    def __init__(self,lenght):
        self.lenght = lenght
    def val(self):
        return self.lenght


class AreaCalculator:
    def __init__(self,arr = []):
        self.arr = arr

    def sum(self):
        return sum(self.arr)

    def output(self):
        return self.sum()


shapes = [Circle(2).val(),Square(5).val(),Square(6).val()]

