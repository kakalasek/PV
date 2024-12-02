def vytvor_pocitadlo_navstevniku():
    pocet_navstevniku = 0

    def pridej_navstevnika():
        nonlocal pocet_navstevniku
        pocet_navstevniku += 1

        return pocet_navstevniku

    return pridej_navstevnika

pridej_navstevnika = vytvor_pocitadlo_navstevniku()
pocet = pridej_navstevnika()
print(pocet)
pocet = pridej_navstevnika()
print(pocet)
pocet = pridej_navstevnika()
print(pocet)