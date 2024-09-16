from datetime import datetime

def check_year(year: str) -> None:
    current_year = datetime.now().year
    if current_year - int(year):
        pass

def check_month(month: str) -> None:
    pass

def check_day(day: str) -> None:
    pass

def check_date(date_of_birth: str) -> None:
    pass

def check_format(date_of_birth: str) -> None:
    if (len(date_of_birth.split(".")) != 3 or not date_of_birth.split(".")[0].isnumeric() or not date_of_birth.split(".")[1].isnumeric() or not date_of_birth.split(".")[2].isnumeric()):
        raise Exception("Invalid Format")

try:
    date_of_birth = input("Enter the date of your birth in format DD.MM.YYYY:\n")
    
    check_format(date_of_birth)
    check_year(date_of_birth.split(".")[2])
    check_month(date_of_birth.split(".")[1])
    check_day(date_of_birth.split(".")[0])
    check_date(date_of_birth)

except Exception as e:
    print(e)