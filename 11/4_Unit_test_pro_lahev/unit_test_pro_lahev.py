import unittest

class NotOpenError(Exception):
    pass

class Bottle:
    def __init__(self, volume: float):
        # TESTED
        if not((isinstance(volume, float) and not isinstance(volume, int)) or (isinstance(volume, int) and not isinstance(volume, float))):
            raise TypeError("Volume must be float or int")

        if volume <= 0.1:
            raise ValueError("Bottle volume must be greater than tenth of a liter")
        self.volume = volume
        self.fullness = 0.0
        self.open = True

    def get_fullness_in_liters(self) -> float:
        return self.fullness
    
    def set_fullness_in_liters(self, fullness) -> None:
        if not((isinstance(fullness, float) and not isinstance(fullness, int)) or (isinstance(fullness, int) and not isinstance(fullness, float))):
            raise TypeError("Fullness must be float or int") # TESTED
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
        if not((isinstance(fullness, float) and not isinstance(fullness, int)) or (isinstance(fullness, int) and not isinstance(fullness, float))):
            raise TypeError("Fullness must be float or int")    # TESTED
        if fullness/1000 > self.volume or fullness < 0:
            raise ValueError("Fullness must be less or equal to the volume of the bottle and cannot be negative")
        if not self.open:
            raise NotOpenError("You must first open the bottle in order to change its fullness")
        
        self.fullness = fullness/1000

    def toggle_bottle(self) -> None:
        self.open = not self.open


class TestLahve(unittest.TestCase):
    def test_creation(self):
        bottle = Bottle(100)
        bottle = Bottle(100.1)
        bottle = Bottle(True)

        with self.assertRaises(TypeError):
            bottle = Bottle("volume")
        with self.assertRaises(TypeError):
            bottle = Bottle([100])
        with self.assertRaises(TypeError):
            bottle = Bottle((100,))
        with self.assertRaises(TypeError):
            bottle = Bottle({100})
        with self.assertRaises(TypeError):
            bottle = Bottle({"volume": 100})
        
        with self.assertRaises(ValueError):
            bottle = Bottle(0.1)
        with self.assertRaises(ValueError):
            bottle = Bottle(-0.1)

    def test_fullness(self):
        bottle = Bottle(100)
        bottle.set_fullness_in_liters(100)

        self.assertEqual(bottle.get_fullness_in_liters(), 100)
        self.assertEqual(bottle.get_fullness_in_milis(), 100e3)

        bottle.set_fullness_in_milis(50e3)
        
        self.assertEqual(bottle.get_fullness_in_liters(), 50)
        self.assertEqual(bottle.get_fullness_in_milis(), 50e3)

        bottle.set_fullness_in_liters(0.3)

        self.assertEqual(bottle.get_fullness_in_liters(), 0.3)
        self.assertEqual(bottle.get_fullness_in_milis(), 300)

        bottle.set_fullness_in_liters(True)

        self.assertEqual(bottle.get_fullness_in_liters(), 1)
        self.assertEqual(bottle.get_fullness_in_milis(), 1e3)

        bottle.empty_bottle()

        self.assertEqual(bottle.get_fullness_in_liters(), 0)
        self.assertEqual(bottle.get_fullness_in_milis(), 0)

        bottle.toggle_bottle()

        with self.assertRaises(NotOpenError):
            bottle.set_fullness_in_liters(100)
        with self.assertRaises(NotOpenError):
            bottle.set_fullness_in_milis(10e3)
        with self.assertRaises(NotOpenError):
            bottle.empty_bottle()

        bottle.toggle_bottle()

        with self.assertRaises(TypeError):
            bottle.set_fullness_in_liters("100")
        with self.assertRaises(TypeError):
            bottle.set_fullness_in_liters((100,))
        with self.assertRaises(TypeError):
            bottle.set_fullness_in_liters([100])
        with self.assertRaises(TypeError):
            bottle.set_fullness_in_liters({100})
        with self.assertRaises(TypeError):
            bottle.set_fullness_in_liters({"fullness": 100})

        with self.assertRaises(TypeError):
            bottle.set_fullness_in_milis("100")
        with self.assertRaises(TypeError):
            bottle.set_fullness_in_milis((100,))
        with self.assertRaises(TypeError):
            bottle.set_fullness_in_milis([100])
        with self.assertRaises(TypeError):
            bottle.set_fullness_in_milis({100})
        with self.assertRaises(TypeError):
            bottle.set_fullness_in_milis({"fullness": 100})

        with self.assertRaises(ValueError):
            bottle.set_fullness_in_liters(101)
        with self.assertRaises(ValueError):
            bottle.set_fullness_in_liters(100.1)
        with self.assertRaises(ValueError):
            bottle.set_fullness_in_liters(-10)
        with self.assertRaises(ValueError):
            bottle.set_fullness_in_liters(-0.1)
        
        with self.assertRaises(ValueError):
            bottle.set_fullness_in_liters(101e3)
        with self.assertRaises(ValueError):
            bottle.set_fullness_in_liters(100.1e3)
        with self.assertRaises(ValueError):
            bottle.set_fullness_in_liters(-10e3)
        with self.assertRaises(ValueError):
            bottle.set_fullness_in_liters(-0.1e3)

if __name__ == "__main__":
    unittest.main()
