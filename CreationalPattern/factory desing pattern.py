from abc import ABC, abstractmethod

# This is the base class for all our shapes


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perameter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        return self.height * self.width

    def calculate_perameter(self) -> float:
        return 2 * (self.height + self.width)


class Square(Shape):
    def __init__(self, width) -> None:
        self.width = width

    def calculate_area(self) -> float:
        return self.height * self.width

    def calculate_perameter(self) -> float:
        return self.width ** 4


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    @property
    def calculate_area(self):
        return 3.14 * float(self.radius * self.radius)

    @property
    def calculate_perameter(self):
        return 2 * self.radius * 3.14


"""In factory pattern will help use to hide the
   whole available shapes from client."""


# this is our interface of creation shape.
class ShapFactory:
    def create_shape(self, name):
        if name == "circle":
            radius = float(input("Enter the radius of the circle: "))
            return Circle(radius)
        if name == "square":
            width = float(input("Enter your width here: "))
            return Square(width)
        if name == "rectangle":
            height = float(input("Enter your height here: "))
            width = float(input("Enter your width here: "))
            return Rectangle(height, width)
        else:
            raise ValueError("Invalid shape format")


"""Here client dont know about shap detail, which method contain these shape
just, client can just create and call theme.
"""


def shape_client():
    shape_factory = ShapFactory()
    shape_name = input("Enter your shape name: ")
    shape = shape_factory.create_shape(shape_name)

    print(f"The type of object created: {type(shape)}")
    print(f"The area of this shap: {shape.calculate_area}")


shape_client()
