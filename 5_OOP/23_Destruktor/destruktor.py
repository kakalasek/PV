class Zbozi:

    def __init__(self,nazev):
        self.nazev = nazev

    def __del__(self):
        print("Zbozi "+str(self.nazev)+" bylo vymazano z pameti")

z = Zbozi('mrkev')
me_oblibene_zbozi = z
del z
del me_oblibene_zbozi
print('konec')