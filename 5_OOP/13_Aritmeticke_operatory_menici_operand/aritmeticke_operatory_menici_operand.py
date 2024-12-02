import re

class PenezniHotovost:
    """
    Trida reprezentuje penezni hotovost v urcite mene
    """

    def __init__(self, castka: float, mena: str):
        """
        Pri vytvoreni tridy se musi specifikovat castka a mena, nebo se pouzije defaultnich 0 EUR

        :param castka: Jakekoli realne cislo, muze byt i zaporne
        :param mena: Mena vyjadrena jako tripismeny kod
        :return: Objekt penezni hotovosti
        """
        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')

        self._mena = mena
        self._castka = castka

    def __str__(self):
        """
        Vrati castku a menu jako string
        :return: <castka> <mena>
        """
        return str(self._castka)+" "+self._mena

    def __add__(self, other):
        """
        Pretizeni operatoru + ktere vytvori novy objekt jako vysledek operace scitnai
        :param other: Lze scitat cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace scitani
        """
        if(isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other
            return vysledek

        if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other._castka
            return vysledek

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")


    def __sub__(self, other):
        """
        Pretizeni operatoru - ktere vytvori novy objekt jako vysledek operace odcitani
        :param other: Lze odcitat cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace odcitani
        """
        if(isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka - other
            return vysledek

        if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka - other._castka
            return vysledek

        raise Exception("Penezni hotovost lze odcitat pouze s int,float a hotovosti ve stejne mene")

    def __mul__(self, other):
        """
        Pretizeni operatoru * ktere vytvori novy objekt jako vysledek operace nasobeni
        :param other: Lze nasobit cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace nasobeni
        """
        if(isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka * other
            return vysledek

        if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka * other._castka
            return vysledek

        raise Exception("Penezni hotovost lze nasobit pouze s int,float a hotovosti ve stejne mene")

    def __pow__(self, power, modulo=None):
        """
        Pretizeni operatoru ** ktere vytvori novy objekt jako vysledek operace mocneni

        :param power: exponent, typu int, nebo float, cislo, na ktere umocnujeme zaklad
        :param modulo: vydeli vysledek umocneneni zadanym cislem a vrati zbytek. Musi byt int, nebo float 
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek nastaveny jako vysledek mocneni, popr. modula mocniny
        """
        if((isinstance(power, float) or isinstance(power, int)) and (isinstance(modulo, int) or isinstance(modulo, float) or modulo is None)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka ** power if not modulo else (self._castka ** power) % modulo
            return vysledek

        raise Exception("Penezni hotovost lze umocnit pouze s int,float a hotovosti ve stejne mene")

    def __iadd__(self, other):
        """
        Implementace operatoru += ma za ukol secist hotovost a zachovat puvodni objekt

        :param other: Muze byt int, float nebo trida PenezniHotovost
        :return: Vrace stavajici objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace soucet
        """

        if isinstance(other, float) or isinstance(other, int):
            self._castka += other
            return self
        
        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            self._castka += other._castka
            return self

    def __isub__(self, other):
        """
        Implementace operatoru -= ma za ukol secist hotovost a zachovat puvodni objekt

        :param other: Muze byt int, float nebo trida PenezniHotovost
        :return: Vrace stavajici objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace rozdil 
        """

        if isinstance(other, float) or isinstance(other, int):
            self._castka -= other
            return self
        
        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            self._castka -= other._castka
            return self

    def __truediv__(self, other):
        """
        Implementace operatori /= ma za ukol vydelit hotovost a zachovat puvodni objekt
        :param other: Muze byt int, float nebo trida PenezniHotovost 
        :return: Vraci stavajici objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace deleni
        """
        if(isinstance(other, float) or isinstance(other, int)):
            self._castka /= other
            return self

        if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
            self._castka /= other._castka
            return self

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")

try:
    sto_korun = PenezniHotovost(100, "CZK")
    sto_korun += 100

    print(sto_korun)
except Exception as e:
    print(e)