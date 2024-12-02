def formatuj_cele_jmeno(jmeno, prijmeni):
    return jmeno + " " + prijmeni

def formatuj_zkracene_jmeno(jmeno, prijmeni):
    return jmeno[0] + ". " + prijmeni


def wrapper_velka_pismena(f):
    def formatuj_velka_pismena(jmeno, prijmeni):
        vysledek = f(jmeno,prijmeni)
        return vysledek.upper()
    return formatuj_velka_pismena

cele_jmeno_velkymi = wrapper_velka_pismena(formatuj_cele_jmeno)
print (cele_jmeno_velkymi("jan", "novak"))

zkrace_velkymi = wrapper_velka_pismena(formatuj_zkracene_jmeno)
print (zkrace_velkymi("jan", "novak"))