class ZvysitelnaUrovenInterface:
    def zvysitUroven(self):
        raise NotImplementedError()

class Bojovnik(ZvysitelnaUrovenInterface):
    def __init__(self, sila):
        if type(sila) is not int or sila < 0 or sila > 3:
            raise Exception("Sila bojovnika neni dostatecne dlouhe")

        self.sila = sila

    def zvysitUroven(self):
        if self.sila + 1 > 3:
            raise Exception("Bojovnikova sila nemuze byt vetsi nez 3")
        self.sila = self.sila + 1

class Mag(ZvysitelnaUrovenInterface):
    def __init__(self, bilaMagie, cernaMagie):
        if type(bilaMagie) is not bool:
            raise Exception("Bila magie musi byt True/False")
        if type(cernaMagie) is not bool:
            raise Exception("Cerna magie musi byt True/False")

        self.cernaMagie = cernaMagie
        self.bilaMagie = bilaMagie

    def zvysitUroven(self):
        if self.bilaMagie and self.cernaMagie:
            raise Exception("Tento mag jiz ovlada vsechny mozne magie")
        elif self.bilaMagie and not self.cernaMagie:
            self.cernaMagie = True
        else:
            self.bilaMagie = True

if __name__ == "__main__":
    bobik = Bojovnik(1)
    bobik.zvysitUroven()
    print(bobik.sila)

    martina = Mag(True, False)
    martina.zvysitUroven()
    print(martina.cernaMagie)