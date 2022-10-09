class GasEngine:
    @staticmethod
    def start():
        print("Engine started")


class Car:
    def __init__(self):
        engine = GasEngine()
        engine.start()


car = Car()


