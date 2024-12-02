def generatorRaselinnychJezerCR():
    yield "Chalupské jezírko"
    yield "Velké mechové jezero"
    yield "Jezírko pod Táborem"
    yield "Malé mechové jezíro"
    yield "Rosička"
    raise StopIteration()

print("Krasjova jezera v CR")
for jezero in generatorRaselinnychJezerCR():
    print(jezero)
