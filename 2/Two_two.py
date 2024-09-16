from math import pi

def calculate_content(radius: float) -> float:
    if radius <= 0:
        raise ArithmeticError("Invalid radius")
    
    return pi * (radius**2)

try:
    radius = input("Enter a radius: ")
    print(calculate_content(float(radius)))
except ArithmeticError as e:
    print(e)