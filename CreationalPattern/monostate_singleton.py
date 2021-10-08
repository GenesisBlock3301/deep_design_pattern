class MonoSingleton:
    __shared_state = {}
    def __init__(self) -> None:
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = MonoSingleton()
b1 = MonoSingleton()
b1.x = 4
print(f"b is here{b.__dict__}")
print(f"b1 is here{b1.__dict__}")