from abc import ABC, abstractmethod


#  This is interface for builder.
class HouseBuilder(ABC):

    @abstractmethod
    def set_wall(self, material: str) -> "HouseBuilder":
        pass

    @abstractmethod
    def set_roof(self, material: str) -> "HouseBuilder":
        pass

    @abstractmethod
    def set_door(self, material: str, color: str) -> "HouseBuilder":
        pass

    @abstractmethod
    def set_window(self, material: str, size: str) -> "HouseBuilder":
        pass

    @abstractmethod
    def build(self) -> "House":
        pass


# Targeted class which we want to create.
# A house consist of walls, roof, door and window.
# So we need to give responsibility to make each parts to builder.
class House:
    def __init__(self):
        self.walls: str = ""
        self.roof: str = ""
        self.door = Door()
        self.window = Window()


# Door and window class which we want to create for house.

class Door:
    def __init__(self):
        self.material: str = ""
        self.color: str = ""


class Window:
    def __init__(self):
        self.material: str = ""
        self.size: str = ""


# Interface implementation class(Concrete Builder)

class BasicHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def set_wall(self, material: str) -> "HouseBuilder":
        self.house.walls = material
        return self

    def set_roof(self, material: str) -> "HouseBuilder":
        self.house.door.material = material
        return self

    def set_door(self, material: str, color: str) -> "HouseBuilder":
        self.house.door.material = material
        self.house.door.color = color
        return self

    def set_window(self, material: str, size: str) -> "HouseBuilder":
        self.house.window.material = material
        self.house.window.size = size
        return self

    def build(self) -> "House":
        return self.house


builder = BasicHouseBuilder()
# use this pattern make a chain, class should follow this chain to make house.
house = builder.set_wall("Bricks") \
    .set_roof("Tile") \
    .set_door("Wood", "Brown") \
    .set_window("Glass", "Large") \
    .build()
print(house)
