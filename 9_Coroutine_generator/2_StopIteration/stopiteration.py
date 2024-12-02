def generatorRaselinnychJezerCR():
    yield "Chalupské jezírko"
    yield "Velké mechové jezero"
    raise StopIteration
    yield "Jezírko pod Táborem"
    yield "Malé mechové jezíro"
    yield "Rosička"

print("Krasjova jezera v CR")
for jezero in generatorRaselinnychJezerCR():
    print(jezero)
