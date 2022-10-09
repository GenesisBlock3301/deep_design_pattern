from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def leg_count(self):
        pass


class Lion(Animal):
    def __init__(self, name):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def make_sound(self):
        return 'roar'

    def leg_count(self):
        return 4


class Mouse(Animal):
    def __init__(self, name):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def make_sound(self):
        return 'squeak'

    def leg_count(self):
        return 4


class Snake(Animal):
    def __init__(self, name):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def make_sound(self):
        return 'hiss'

    def leg_count(self):
        return 0


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound(), animal.leg_count())


animals = [
    Lion("Lion"),
    Mouse("Mouse"),
    Snake("Snake")
]
animal_sound(animals)

def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())


animal_leg_count(animals)
# animal_leg_count(animals)