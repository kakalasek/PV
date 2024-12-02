def generatorRaselinnychJezerCR():
    yield "Chalupské jezírko"
    yield "Velké mechové jezero"
    yield "Jezírko pod Táborem"
    yield "Malé mechové jezíro"
    yield "Rosička"

print("Raselinna jezera v CR")
generator = generatorRaselinnychJezerCR()
while True:
    try:
        print(next(generator))
    except:
        break