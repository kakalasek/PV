class NotOpenError(Exception):
    pass

class Bottle:
    def __init__(self, volume: float):
        if not isinstance(volume, float) and not isinstance(volume, int):
            raise TypeError("Volume must be float or int")

        if volume <= 0.1:
            raise ValueError("Bottle volume must be greater than tenth of a liter")
        self.volume = volume
        self.fullness = 0.0
        self.open = True

    def get_fullness_in_liters(self) -> float:
        return self.fullness
    
    def set_fullness_in_liters(self, fullness) -> None:
        if not isinstance(fullness, float) and not isinstance(fullness, int):
            raise TypeError("Fullness must be float or int")
        if fullness > self.volume or fullness < 0:
            raise ValueError("Fullness must be less or equal to the volume of the bottle and cannot be negative")
        if not self.open:
            raise NotOpenError("You must first open the bottle in order to change its fullness")
        
        self.fullness = fullness

    def empty_bottle(self) -> None:
        if not self.open:
            raise NotOpenError("You must first open the bottle in order to change its fullness")
        self.fullness = 0

    def get_fullness_in_milis(self) -> float:
        return self.fullness*1000

    def set_fullness_in_milis(self, fullness) -> None:
        if not isinstance(fullness, float) and not isinstance(fullness, int):
            raise TypeError("Fullness must be float or int")
        if fullness/1000 > self.volume or fullness < 0:
            raise ValueError("Fullness must be less or equal to the volume of the bottle and cannot be negative")
        if not self.open:
            raise NotOpenError("You must first open the bottle in order to change its fullness")
        
        self.fullness = fullness/1000

    def toggle_bottle(self) -> None:
        self.open = not self.open

try:
    bottle1 = Bottle(1)
    bottle1.set_fullness_in_milis(1000)
    print(bottle1.get_fullness_in_milis())
except Exception as e:
    print(e)