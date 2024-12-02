def coulombs_law(Ke: float = None, q1: float = None, q2: float = None, r: float = None):
    """
    Calculates coulombs law. All quantities must be in their basic units
    """

    return Ke*(q1*q2/r**2)