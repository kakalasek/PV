try:
    height: float = float(input('Enter your height in meters:\n'))
    weight: float = float(input('Enter your weight in kilograms:\n'))

    if weight <= 0 or height <= 0:
        raise ValueError

    bmi: float = weight/(height**2)

    print(bmi)

    match bmi:
        case _ if bmi < 18.5:
            print("Underweight")
        case _ if bmi >= 18.5 and bmi <= 25:
            print("Ideal weight")
        case _ if bmi > 25 and bmi <= 30:
            print("Overweight")
        case _ if bmi > 30 and bmi <= 40:
            print("Obesity")
        case _:
            print("Morbid obesity")

    
except ValueError as e:
    print("Entered value is not a valid number")
except ZeroDivisionError as e:
    print("Entered value is not a valid number")
