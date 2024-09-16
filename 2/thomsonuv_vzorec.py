from math import sqrt

while True:
    try:
    
        while True:
            try:
                L = input("Zadej indukcnost [H]:")
                if not L.replace(".", "").replace("-", "").isnumeric():
                    raise TypeError 
                break
            except TypeError as e:
                continue
        while True:
            try:
                C = input("Zadej kapacitu [F]:")
                if not C.replace(".", "").replace("-", "").isnumeric():
                    raise TypeError 
                break
            except TypeError as e:
                continue

        F = 1 / (2 * 3.14 * sqrt(float(L) * float(C)))

        print("Frekvence je: " + str(F) + "Hz")
        break
    except ValueError as e:
        continue