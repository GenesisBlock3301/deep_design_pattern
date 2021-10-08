from abc import ABC, abstractmethod
from createVegNonVegPizza import *

class PizzaFactory(ABC):
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createNonVegPizza(self):
        return DeluxVeggiePizza()

    def createVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createNonVegPizza(self):
        return MexicanVeggiePizza()

    def createVegPizza(self):
        return HamPizza()
