
class Vehicle:
    def go(self):
        print("Now I'm driving..")


class StreetRacer(Vehicle):
    pass

class FormulaOne(Vehicle):
    pass

class Halicaptar(Vehicle):
    def go(self):
        print("Now I'm flying")

class Jet(Vehicle):
    def go(self):
        print("Now I'm flying")




streetRacer = StreetRacer()
formulaOne = FormulaOne()
halicaptar = Halicaptar()
jet = Jet()

streetRacer.go()
formulaOne.go()
halicaptar.go()
jet.go()