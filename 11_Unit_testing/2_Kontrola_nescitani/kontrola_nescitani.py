import unittest

def scitani(a, b):
    if (not a and not b) or (isinstance(a, list) and isinstance(b, list)):
        raise TypeError
    if (isinstance(a, float) ^ isinstance(a, int) ^ isinstance(a, complex)) and (isinstance(b, float) ^ isinstance(b, int) ^ isinstance(b, complex)):
        return a + b
    raise ValueError

class TestScitani(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(scitani(1, 1), 2)
        self.assertEqual(scitani(2.5, 1.5), 4)
        self.assertEqual(scitani(1j, 1j), 2j)

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            scitani("AHOJ", 100)
        with self.assertRaises(ValueError):
            scitani(100, "AHOJ")
        with self.assertRaises(TypeError):
            scitani(None, None)
        with self.assertRaises(TypeError):
            scitani([4,5,6], [1,2,3])
        with self.assertRaises(ValueError):
            scitani({"hello": 10}, {"Ahoj": 20})
        with self.assertRaises(ValueError):
            scitani((1, 2, 3), (3, 5, 1))
        with self.assertRaises(ValueError):
            scitani({1, 4, 2}, {4, 12, 1})


if __name__ == "__main__":
    unittest.main()