while True:
    print("Ahoj, jak se jmenuješ?")

    name: str = input()

    print(f"Opravdu se jmenuješ: {name}?")

    decision = input()

    if decision.isnumeric():
        if int(decision):
            print("Sbohem")
            break