def generatorSudychCisel(od, do):
    i = od
    if i % 2 == 1:
        i = i + 1
    while (i < do):
        yield i
        i = i + 2

for x in generatorSudychCisel(1, 50):
    print(x)