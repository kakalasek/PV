def isDay(day: str) -> bool:
    if day.isnumeric() and not len(day) > 2 and not int(day) > 31:
        return True
    return False

def isMonth(month: str) -> bool:
    if month.isnumeric() and not len(month) > 2 and not int(month) > 12:
        return True
    return False

def isYear(year: str) -> bool:
    if year.isnumeric() and not len(year) > 4 and not int(year) > 2024:
        return True
    return False

while True:
    day = input('Enter the day of your birth:\n')
    if not isDay(day):
        print('Invalid input')
        continue
    month = input('Enter the month of your birth:\n')
    if not isMonth(month):
        print('Invalid input')
        continue
    year = input('Enter the year of your birth:\n')
    if not isYear(year):
        print('Invalid input')
        continue
    break

print(f'{day}.{month}.{year}')