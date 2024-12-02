def ohms_law(I: float = None, U: float = None, R: float = None) -> tuple:
    """
    Calculates the undefined part of ohms law. All quantities are in their basic unit (Amperes, Volts, Ohms)

    :param A: Electrical current
    :param U: Voltage
    :param R: Resistance 
    :return: Tuple in this format (I, U, R)
    """

    if I and U and R:
        return (I, U, R)
    
    if I and U and not R:
        R = U/I
        return (I, U, R)
    if U and R and not I:
        I = U/R
        return (I, U, R)
    if I and R and not U:
        U = I * R
        return (I, U, R)

    raise Exception("Not enough quantities are set. Not all can be calculated")


def coulombs_law(Ke: float = None, q1: float = None, q2: float = None, r: float = None):
    """
    Calculates coulombs law. All quantities must be in their basic units
    """

    return Ke*(q1*q2/r**2)