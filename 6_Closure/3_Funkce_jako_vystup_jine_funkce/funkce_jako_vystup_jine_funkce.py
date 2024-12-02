def format_surname_first(name: str, surname: str) -> str:
    return surname + " " + name

def format_monogram(name: str, surname: str) -> str:
    return name[0] + "." + surname[0] + "."


def choose_formatting_function(lenth: int):
    if lenth < 4:
        return format_monogram
    return format_surname_first

formatter = choose_formatting_function(150)
print(formatter("Jan", "Novak"))