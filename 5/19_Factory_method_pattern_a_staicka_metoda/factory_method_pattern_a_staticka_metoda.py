class Firma:
    """ Třída reprezentuje firmu"""

    @staticmethod
    def factory_from_obchodni_nazev(obchodni_nazev: str):
        data = obchodni_nazev.split(', ')

        if(len(data) != 2):
            raise Exception("Nelze parsovat obchodni nazev")
        
        return Firma(data[0], data[1])

    def __init__(self, nazev, pravni_forma):
        """
        Vytvoří instanci firmy
        :param nazev: Název například Maso a uzeniny od Pavlíka
        :param pravni_forma: Právní forma, například s.r.o, nebo a.s. apod.
        """
        self.jmeno = nazev
        self.pravni_forma = pravni_forma


sporka = Firma.factory_from_obchodni_nazev("Česká spořitelna, a.s.")
print(sporka.pravni_forma) #ma vypsat "a.s."

