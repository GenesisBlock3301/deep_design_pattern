from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def __init__(self, name):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def __init__(self, name):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def __init__(self, name):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def make_sound(self):
        return 'hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [
    Lion("Lion"),
    Mouse("Mouse"),
    Snake("Snake")
]
animal_sound(animals)