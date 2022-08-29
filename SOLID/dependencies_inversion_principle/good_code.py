from abc import ABC, abstractmethod


class Eatable(ABC):
    def eat(self):
        return NotImplemented


class Apple(Eatable):
    def eat(self):
        print(f"Eating apple. Transferring {5} unit energy to brain.")


class Chocolate(Eatable):
    def eat(self):
        print(f"Eating chocolate")


class Robot:
    def get_energy(self, eatable: Eatable):
        eatable.eat()


if __name__ == "__main__":
    robot = Robot()
    robot.get_energy(Apple())
    robot.get_energy(Chocolate())
