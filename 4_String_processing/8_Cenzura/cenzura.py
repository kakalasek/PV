import re

def create_sql(author: str, text: str) -> str:

    list_of_censored_names = [
        'Ondřej Mandík',
        'Alena Reichlová',
        'Jára Cimrman'
    ]

    censored_names_regex = f"((Ondra|Ondřej|)[ ]*Mandík|(Alena|)[ ]*Reichlová|(Jaroslav|Jára|)[ ]*Cimrman)"

    if not re.match(r"^[a-zA-Z]{1}[a-zA-Z' -]*[a-zA-z]$", author):
        raise ValueError("Invalid author")



    for name in list_of_censored_names:
        while True:
            appearence = re.search(censored_names_regex, text)
            if appearence:
                text = text.replace(appearence.group().strip(), "Automatically censored", 1)
                continue
            break

    return f"INSERT INTO PRISPEVEK(AUTHOR, TEXT) VALUES ('{author}', '{text}')"

try:
    statement = create_sql("O'Connor", "Alena Reichlová a Mandík je dvojice plna .. no nic")
    print(statement)
except ValueError as e:
    print(e)