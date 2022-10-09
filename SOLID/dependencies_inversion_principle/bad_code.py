class Apple:
    def eat(self):
        print(f"Eating apple. Transferring {5} unit energy to brain.")


class Chocolate:
    def eat(self):
        print(f"Eating chocolate")


class Robot:
    def get_energy(self, eatable: str):
        if eatable == "Apple":
            apple = Apple()
            apple.eat()
        elif eatable == "Chocolate":
            chocolate = Chocolate()
            chocolate.eat()


if __name__ == "__main__":
    robot = Robot()
    robot.get_energy("Chocolate")