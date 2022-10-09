from abc import ABC, abstractmethod


class IEngine(ABC):
    @abstractmethod
    def start(self):
        pass


class GasEngine(IEngine):
    def start(self):
        print("Start gas engine")


class ElectricEngine(IEngine):
    def start(self):
        print("Start electric engine")


class Car:
    def __init__(self, engine: IEngine):
        self.engine = engine

    def run(self):
        return self.engine.start()


car1 = Car(engine=GasEngine())
car1.run()

car2 = Car(engine=ElectricEngine())
car2.run()
