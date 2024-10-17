class Rectangle():
    """
    This class represents a rectangle 
    """

    def __init__(self, a, b):
        """
        This method creates the rectangle

        :param a: Side 'a' of the rectangle
        :param b: Side 'b' of the rectangle 
        """
        if (not isinstance(a, int) and not isinstance(a, float)) or (not isinstance(b, int) and not isinstance(b, float)):
            raise TypeError("'a' and 'b' must be either int or float")

        if  a <= 0 or b <= 0:
            raise ValueError("'a' and 'b' must be a positive int or float")

        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b
    
    @a.setter
    def a(self, a):
        if not isinstance(a, int) or not isinstance(a, float):
            raise TypeError("'a' must be either an int or float")
        if a >= 0:
            raise ValueError("'a' must be a positive int or float")
        self._a = a
    
    @b.setter
    def b(self, b):
        if not isinstance(b, int) or not isinstance(b, float):
            raise TypeError("'b' must be either an int or float")
        if b >= 0:
            raise ValueError("'b' must be a positive int or float")
        self._b = b

square = Rectangle(-1.2, 5) 