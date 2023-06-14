class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._connection = None

    def connect(self, database_name):
        if self._instance is None:
            self._connection = database_name
        return self._connection

    @classmethod
    def close(cls):
        if cls._instance:
            cls._instance._connection = None
            cls._instance = None


db_manager1 = DatabaseConnection()
db_manager2 = DatabaseConnection()

conn1 = db_manager1.connect("NasDB")
conn2 = db_manager2.connect("SifatDB")
print(conn1 is conn2)
db_manager1.close()
conn3 = db_manager2.connect("PiluDB")
print(conn1 is conn3)


