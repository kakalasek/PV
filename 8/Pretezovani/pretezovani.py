import re

class Zbozi:
    def __init__(self, nazev, cena):
        """
        Nastavi cenu a nazev zbozi
        :param nazev: str Nazev jen znaky anglicke abecedy 2-50
        :param cena: float 0 az 1mio, kladne cislo
        """
        if type(nazev) is not str or not re.match(r"[a-zA-Z]{2,50}", nazev):
            raise Exception('Nazev musi byt 2-50 znaku')
        if (type(cena) is not float and type(cena) is not int) or cena < 0:
            raise Exception('Nazev musi byt 2-50 znaku')
        self._nazev = nazev
        self._cena = cena

    def get_cena(self):
        """
        Vrati cenu
        :return: int
        """
        return self._cena
    
class ZlevneneZbozi(Zbozi):
    def __init__(self, nazev, cena, sleva):
        if sleva < 0 or sleva > 1:
            raise Exception("Sleva musi byt v procentech, tj. od 0 do 1")
        super().__init__(nazev, cena)
        self._sleva = sleva

    def get_cena(self):
        return self._cena - (self._sleva * self._cena)
    
tycinka = ZlevneneZbozi('margot', 15, 0.2)
print(tycinka.get_cena())
        