import datetime

def check_format(date_of_birth: str) -> None:
    if (len(date_of_birth.split(".")) == 3):
        day: str = date_of_birth.split(".")[0]
        month: str = date_of_birth.split(".")[1]
        year: str = date_of_birth.split(".")[2]

        if (not day.isnumeric() or not month.isnumeric() or not year.isnumeric()):
            raise Exception("Invalid Format")
    else:
        raise Exception("Invalid Format")
    
    return day, month, year

try:
    date_of_birth = input("Enter the date of your birth in format DD.MM.YYYY:\n")
    
    day, month, year = check_format(date_of_birth)
    date_of_birth_formatted = datetime.datetime(int(year), int(month), int(day))

    year_difference = datetime.datetime.now().year - date_of_birth_formatted.year
    if year_difference < 0 or year_difference > 119:
        raise Exception("Invalid year of birth -> You must be from 0 to 119 year old")
    
    # Month and day restrictions are handled by the datetime library for me :)

    if date_of_birth_formatted.month == 7 or date_of_birth_formatted.month == 8:
        raise Exception(f"You surely could not be born in this date: {date_of_birth_formatted.date()}")
    
    print("Everything went okay :]")

except Exception as e:
    print(e)