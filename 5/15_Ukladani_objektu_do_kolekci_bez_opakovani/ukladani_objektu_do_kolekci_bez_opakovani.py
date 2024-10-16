import re

class Zbozi:
    """ Trida zbozi pro ukazu prikladu relacnich operatoru"""

    def __init__(self, nazev: str, vaha: float):
        """
        Pri vytvoreni se nastavuje nazev zbozi a jeho vaha

        :param nazev: Nazev musi byt znaky v rozsahu 1 az 200 znaku
        :param vaha: Vaha musi byt kladne a nenulove cislo
        """
        if not re.match(r"^[\D ]{1,200}$", nazev):
            raise Exception('Nazev musi byt v rozsahu 1 az 200 znaku')
        if vaha <= 0:
            raise Exception('Vaha nesmi byt zapojna')

        self._nazev = nazev
        self._vaha = vaha

    def __lt__(self, other):
        """
        Metoda zjistuje jestli je zbozi mensi nez druhe zbozi. Porovnava se pouze vaha.

        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self mensi nez other
        """
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha < other._vaha
    
    def __gt__(self, other):
        """
        Metoda zjistuje, jestli je zbozi vetsi nez druhe zbozi. Porovnava se pouze vaha

        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self vetsi nez other
        """
        if not isinstance(other, Zbozi):
            raise Exception('Porovnanvat lze jen zbozi mezi sebou')
        
        return self._vaha > other._vaha

    def __eq__(self, other):
        """
        Metoda zjistuje, jestli je si zbozi rovno. Porovnava se pouze vaha

        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self rovno other
        """
        if not isinstance(other, Zbozi):
            raise Exception('Porovnanvat lze jen zbozi mezi sebou')
        
        return self._vaha == other._vaha 
    
zbozi1 = Zbozi("Mrkev", 1)
print(hash(zbozi1))