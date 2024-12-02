class KonfiguraceKonference:

    _maximalni_pocet_ucastniku = 0

    def __new__(cls):
        raise NotImplementedError("You cannot create an instance of this object")


    @classmethod
    def set_maximalni_pocet_ucastniku(cls, max):
        cls._maximalni_pocet_ucastniku = max

    @classmethod
    def get_maximalni_pocet_ucastniku(cls):
        return cls._maximalni_pocet_ucastniku
    
print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())

KonfiguraceKonference.set_maximalni_pocet_ucastniku(212)
print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())

try:
    mojeKonfigurace = KonfiguraceKonference()
    mojeKonfigurace.set_maximalni_pocet_ucastniku(300)
    print(mojeKonfigurace.get_maximalni_pocet_ucastniku())
except Exception as e:
    print(e)