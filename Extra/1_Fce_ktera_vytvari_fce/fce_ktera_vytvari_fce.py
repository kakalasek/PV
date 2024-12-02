def generuj_pricitaci_funkci(krok):
    def pricitej(cislo):
        return cislo+krok
    return pricitej

def generuj_nasobici_funkci(krok):
    def nasob(cislo):
        return cislo*krok
    return nasob

nasob_nulou = generuj_nasobici_funkci(0)
nasob_jednickou = generuj_nasobici_funkci(1)
nasob_minus_jednickou = generuj_nasobici_funkci(-1)
nasob_sedmnactkou = generuj_nasobici_funkci(17)
nasob_devet_set_devitkou = generuj_nasobici_funkci(919)

print(nasob_nulou(20))
print(nasob_jednickou(20))
print(nasob_minus_jednickou(20))
print(nasob_sedmnactkou(20))
print(nasob_devet_set_devitkou(20))
