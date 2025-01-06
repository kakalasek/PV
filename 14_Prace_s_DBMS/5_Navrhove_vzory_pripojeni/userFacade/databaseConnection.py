
class DatabaseConnection():

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(DatabaseConnection, cls).__new__(cls)
        return cls.instance
    
    
