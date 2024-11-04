import math


class OhmLaw:

    def count_curent(u : float, r: float):
        """
        Function will count current
        :param u: Voltage you have
        :param r: Resistance you have
        :return: Current you want to count
        """
        return str(u/r)

    def count_resistance(u : float, i : float):
        """
        Function will count resistance
        :param u: Voltage you have
        :param i: Current you have
        :return: Resistance you want to count
        """
        return u/i

    def count_voltage(i: float, r: float):
        """
        Function will count voltage
        :param i: Current you have
        :param r: Resistance you have
        :return: Voltage you want to count
        """
        return i*r

class CoulombLaw:
    def count_force(Q1: float, Q2: float, r : float, Er: float):
        output = (1/ (4*Er*math.pi)) * ((Q1* Q2)/ (r * r))
        return output