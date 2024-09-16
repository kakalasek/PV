while True:
    try:
        x = input("Enter a number: ")
        if not x.isnumeric():
            raise TypeError
        y = int(x) + 1
        print(y)
        break
    except TypeError as e:
        continue