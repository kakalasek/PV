try:
    height: int = int(input('Enter your height:\n'))
    weight: int = int(input('Enter your weight:\n'))

    
except ValueError as e:
    print("Entered value is not a number")
