def wrapper_velka_pismena(f):
    def formatuj_velka_pismena(jmeno, prijmeni):
        vysledek = f(jmeno,prijmeni)
        return vysledek.upper()
    return formatuj_velka_pismena

@wrapper_velka_pismena
def formatuj_cele_jmeno(jmeno, prijmeni):
    return jmeno + " " + prijmeni

@wrapper_velka_pismena
def formatuj_zkracene_jmeno(jmeno, prijmeni):
    return jmeno[0] + ". " + prijmeni



print (formatuj_cele_jmeno("jan", "novak"))

print (formatuj_zkracene_jmeno("jan", "novak"))