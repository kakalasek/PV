import re

def create_sql(author: str, text: str) -> str:
    if not re.match(r"(?!.*?(['-]).*?\1)[a-zA-Z]{1}[a-zA-Z'-]*[a-zA-z]$", author):
        raise ValueError("Invalid author")
    
    if not re.match("",text):
        pass

    author = author.replace("'", "\\'")
    text = text.replace('\\', "\\\\")
    text = text.replace('"', '\\"')
    text = text.replace("'", "\\'")

    return f"INSERT INTO PRISPEVEK(AUTHOR, TEXT) VALUES ('{author}', '{text})')"

try:
    author = input("Enter name: ")
    text = input("Enter text: ")
    statement = create_sql(author, text)
    print(statement)
except ValueError as e:
    print(e)