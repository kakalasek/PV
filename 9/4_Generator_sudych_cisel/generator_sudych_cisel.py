def generatorSudychCisel(od, do):
    i = od
    while (i < do):
        yield i
        i = i + 1
        if i % 2 == 1:
            i = i + 1

for x in generatorSudychCisel(1, 50):
    print(x)