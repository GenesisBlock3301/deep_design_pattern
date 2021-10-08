# 1. We will allow the creation of only one instance of the Singleton class.
# 2. If an instance exists, we will serve the same object again.
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls,'__obj'):
            cls.__obj = super(Singleton,cls).__new__(cls)
            # print(cls.__obj)
        return cls.__obj


s = Singleton()

print("Object created S",s)

s1 = Singleton()
print("Object created s1",s1)


