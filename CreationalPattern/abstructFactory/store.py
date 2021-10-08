from CountryPizzaFactory import *


class PizzaStore:
    def __init__(self) -> None:
        pass

    def makePizza(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizza()
