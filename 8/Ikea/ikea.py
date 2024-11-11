class IkeaItem:
    def __init__(self, shelf_number, aisle_number, name, price):
        if shelf_number > 100 or shelf_number < 1:
            raise Exception("Shelf number must be between 1 and 100")
        if aisle_number not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
            raise Exception("Aisle number must be A-K")
        
        self.shelf_number = shelf_number
        self.aisle_number = aisle_number
        self.name = name
        self.price = price


class lack(IkeaItem):
    def __init__(self, shelf_number, aisle_number, name, price, color):
        super().__init__(self, shelf_number, aisle_number, name, price)
        self.color = color

class samla_box(IkeaItem):
    def __init__(self, shelf_number, aisle_number, name, price, volume):
        super().__init__(self, shelf_number, aisle_number, name, price)
        self.volume = volume

class sjorapport(IkeaItem):
    def __init__(self, shelf_number, aisle_number, name, price, expiration, weight):
        super().__init__(self, shelf_number, aisle_number, name, price)
        self.expiration = expiration
        self.weight = weight