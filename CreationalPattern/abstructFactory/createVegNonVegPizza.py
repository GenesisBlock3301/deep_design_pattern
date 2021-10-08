from typing import AbstractSet


from abc import ABC, abstractmethod


class vegPizza(ABC):
    @abstractmethod
    def prepare(self, vegPizza):
        pass


class NonvegPizza(ABC):
    @abstractmethod
    def serve(self, vegPizza):
        pass


class DeluxVeggiePizza(vegPizza):
    def prepare(self):
        print(f"Prepare {type(self).__name__}")


class ChickenPizza(NonvegPizza):
    def serve(self,VegPizza):
        print(
            f"{type(self).__name__} is served with chicken on -- {type(VegPizza).__name__}"
        )


class MexicanVeggiePizza(vegPizza):
    def prepare(self):
        print(f"Prepare {type(self).__name__}")


class HamPizza(NonvegPizza):
    def serve(self):
        print(
            f"{type(self).__name__} is served with chicken on -- {type(vegPizza).__name__}"
        )
