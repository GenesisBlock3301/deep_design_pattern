class Singleton:
    __instance = None
    def __init__(self) -> None:
        if not Singleton.__instance:
            print("__init__ method call")
        else:
            print("Instance already created",self.getIntance())
    
    @classmethod
    def getIntance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()
s.getIntance()
s1 = Singleton()
# s1.getIntance()