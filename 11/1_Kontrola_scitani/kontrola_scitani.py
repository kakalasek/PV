import unittest

def scitani(a, b):
    return a + b

class TestScitani(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(scitani(1, 1), 2)
        self.assertEqual(scitani(2.5, 1.5), 4)
        self.assertEqual(scitani(1j, 1j), 2j)

if __name__ == "__main__":
    unittest.main()