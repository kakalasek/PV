from re import match

def change_phone(username: str, phone: str) -> str:
    if not match(r"(?!--)[a-zA-Z]{1}[a-zA-Z' -]*[a-zA-z]$", username):
            raise ValueError("Invalid author")
    
    username = username.replace("'", "\\'")
    
    if not match(r"\d{9}", phone):
          raise ValueError("Invalid phone number")
    
    return f"UPDATE USER SET PHONE = '{phone}' WHERE USERNAME = '{username}';"
try:
    print(change_phone('O\'Connor', '874222423'))
except Exception as e:
      print(e)