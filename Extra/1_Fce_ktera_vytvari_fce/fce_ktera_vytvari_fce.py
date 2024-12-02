def generuj_pricitaci_funkci(krok):
    def pricitej(cislo):
        return cislo+krok
    return pricitej

x = generuj_pricitaci_funkci(5)
y = generuj_pricitaci_funkci(-1)

print(x(1))
print(x(2))
print(x(3))

print(y(1))
print(y(2))
print(y(3))