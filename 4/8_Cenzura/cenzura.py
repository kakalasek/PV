import re

def create_sql(author: str, text: str) -> str:

    list_of_censored_names = [
        'Ondřej Mandík',
        'Alena Reichlová',
        'Jára Cimrman'
    ]

    censored_names_regex = f""

    if not re.match(r"^[a-zA-Z]{1}[a-zA-Z'- ]*[a-zA-z]$", author):
        raise ValueError("Invalid author")



    for name in list_of_censored_names:
        while True:

            appearence = re.search(censored_names_regex, text)

    return f"INSERT INTO PRISPEVEK(AUTHOR, TEXT) VALUES ('{author}', '{text}')"

try:
    statement = create_sql("O'Connor", "Alena Reichlová a Mandík")
    print(statement)
except ValueError as e:
    print(e)