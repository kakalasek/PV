from math import sqrt
from cmath import sqrt as csqrt

def calculate_discriminant(a: int, b: int, c: int) -> int:
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        raise ArithmeticError
    return discriminant


discriminant = 0
results = []
a = 12
b = 15
c = 1 

try:
    discriminant = calculate_discriminant(a, b, c)
except ArithmeticError as e:
    results.append((-b+sqrt(discriminant))/(2*a))
    results.append((-b-sqrt(discriminant))/(2*a))
else:
    if discriminant == 0:
        results.append((-b)/(2*a))
    else:
        results.append((-b+csqrt(discriminant))/(2*a))
        results.append((-b-csqrt(discriminant))/(2*a))
finally:
    for result in results:
        print(f"Result: {result}")