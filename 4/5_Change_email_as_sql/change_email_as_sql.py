from re import match

def update_email(username: str, email: str) -> str:
    if not match(r"(?!--)[a-zA-Z]{1}[a-zA-Z' -]*[a-zA-z]$", username):
            raise ValueError("Invalid username")

    username = username.replace("'", "\\'")

    if not match(r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$", email):
          raise ValueError("Invalid email")

    return f"UPDATE ACCOUNT SET EMAIL = '{email}' WHERE USERNAME = '{username}';"

try:
    print(update_email("Pepa", "pepa@seznam.cz"))
except Exception as e:
      print(e)