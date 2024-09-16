def calculate_resistance(U: float, I: float) -> float:
    raise NotImplementedError

def calculate_voltage(R: float, I: float) -> float:
    return R * I 

def calculate_current(R: float, U: float) -> float:
    raise NotImplementedError

try:
    print("Leave one quantity empty. That will be the one calculated by the program")
    R = input("Enter resistance: ")
    I = input("Enter current: ")
    U = input("Enter voltage: ")

    match R, I, U:
        case _ if R and I and U:
            raise Exception('You have not left out one value')
        case _ if R and I and not U:
            print(calculate_voltage(float(R), float(I)))
        case _ if R and U and not I:
            print(calculate_current(float(R), float(U)))
        case _ if U and I and not R:
            print(calculate_resistance(float(U), float(I)))
        case _:
            raise Exception("You have left out more than one value")

except NotImplementedError as e:
    print("Not implemented yet")
except ValueError as e:
    print("One of the entered values was not a valid number")
except Exception as e:
    print(e)