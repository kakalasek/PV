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

class MeasureableIkeaItem():
    def __init__(self, size_x, size_y, size_z):
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z

class PlasticWasteIkeaItem():
    def __init__(self, plastic_weight):
        self.plastic_weight = plastic_weight

class Lack(IkeaItem, MeasureableIkeaItem):
    def __init__(self, shelf_number, aisle_number, name, price, color, size_x, size_y, size_z):
        IkeaItem.__init__(self, shelf_number, aisle_number, name, price)
        MeasureableIkeaItem.__init__(self, size_x, size_y, size_z)
        self.color = color

class Samla_box(IkeaItem, MeasureableIkeaItem, PlasticWasteIkeaItem):
    def __init__(self, shelf_number, aisle_number, name, price, volume, size_x, size_y, size_z, plastic_weight):
        IkeaItem.__init__(self, shelf_number, aisle_number, name, price)
        MeasureableIkeaItem.__init__(self, size_x, size_y, size_z)
        PlasticWasteIkeaItem.__init__(self, plastic_weight)
        self.volume = volume

class Sjorapport(IkeaItem, PlasticWasteIkeaItem):
    def __init__(self, shelf_number, aisle_number, name, price, expiration, weight, plastic_weight):
        IkeaItem.__init__(self, shelf_number, aisle_number, name, price)
        PlasticWasteIkeaItem.__init__(self, plastic_weight) 
        self.expiration = expiration
        self.weight = weight
if __name__ == '__main__':
    samla = Samla_box(15, 'K', 'samla box big', 700, 50, 10, 5, 20, 30)
    lack = Lack(14, 'K', 'lack small', 150, 'green', 20, 30, 20)
    sjorapport =  Sjorapport(3, 'D', 'sjor medium', 300, '2025-07-04', 150, 20)

    print(samla.plastic_weight)
    print(lack.size_z)
    print(sjorapport.name)