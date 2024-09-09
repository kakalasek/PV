number_of_tries = 3
pin = "1111"

while number_of_tries:
    pin_guess = input("Enter your PIN:\n")

    if pin == pin_guess:
        print("Correct PIN, Congrats!")
        break
    else:
        print("Incorrect PIN!")
        number_of_tries = number_of_tries - 1
        if not number_of_tries:
            print("You ran out of tries")