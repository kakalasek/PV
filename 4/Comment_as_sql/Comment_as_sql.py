import re

def create_sql(author: str, text: str) -> str:
    if not re.match(r"^[a-zA-Z]{1}[a-zA-Z'- ]*[a-zA-z]$", author):
        raise ValueError("Invalid author")

    return f"INSERT INTO PRISPEVEK(AUTHOR, TEXT) VALUES ('{author}', '{text}')"

try:
    statement = create_sql("O'Connor", "Text")
    print(statement)
except ValueError as e:
    print(e)