class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def log(self, message):
        print(f"Logging: {message}")


instance1 = Logger()
instance2 = Logger()

instance1.log("Message 1")
instance2.log("Message 2")
