from abc import ABC, abstractmethod


class GoAlgorithm(ABC):
    @abstractmethod
    def go(self):
        pass


# sperate algorithm each vehicle
class GoDrivingAlgorithm(GoAlgorithm):
    def go(self):
        print("Now I'm Driving..")


class GoByFlying(GoAlgorithm):
    def go(self):
        print("Now I'm Flying 200mph..")


class GoByFlyingFast(GoAlgorithm):
    def go(self):
        print("Now I'm Flying Fast..")


# composite class
class Vehicle:

    def __init__(self) -> None:
        pass

    def setAlgorithm(self, algorithm):
        self.goAlgorithm = algorithm

    def go(self):
        self.goAlgorithm.go()


class StreetRacer(Vehicle):
    def __init__(self, algorithm) -> None:
        Vehicle()
        self.setAlgorithm(algorithm)


class Halicaptor(Vehicle):
    def __init__(self, algorithm) -> None:
        Vehicle()
        self.setAlgorithm(algorithm)


class Jet(Vehicle):
    def __init__(self, algorithm) -> None:
        Vehicle()
        self.setAlgorithm(algorithm)


class RealJet:

    def __init__(self) -> None:
        self.rjet = Jet(GoByFlyingFast())
        self.rjet.go()
        self.rjet = Jet(GoDrivingAlgorithm())
        self.rjet.go()


streetRacer = StreetRacer(GoDrivingAlgorithm())
halicaptor = Halicaptor(GoByFlying())
jet = Jet(GoByFlyingFast())

streetRacer.go()
halicaptor.go()
jet.go()
print("---real jet")
RealJet()
print("---real jet")
RealJet()
