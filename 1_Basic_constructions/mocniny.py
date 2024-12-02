import math

while True:
    exponent = input("Enter the exponent:\n")
    if not exponent.isnumeric():
        print('Invalid Input')
        continue
    else:
        exponent = int(exponent)

    if exponent <= 0:
        print('Invalid Input')
        continue

    base = input("Enter the base:\n")
    if not base.lstrip('-').isnumeric():
        print('Invalid Input')
        continue
    else:
        base = int(base)

    print(math.pow(base,exponent))
    break
