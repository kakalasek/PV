def generatorITVelikanu():
    yield "Linus Torvalds"
    yield "Ken Thompson"
    yield "Dennis Ritchie"

print("Velikáni v IT")
for osoba in generatorITVelikanu():
    print(osoba)