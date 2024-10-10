from re import match

def password_policy_check(username: str, password: str) -> None:

    password_regex = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[`~!@$#%^&*()_+\-=\[\]{}\\'\";:\/.>,<])(?!.*" + username + r")[a-zA-Z\d`~!@$#%^&*()_+\-=\[\]{}\\'\";:\/.>,<]{10,}$"

    if not match(password_regex, password):
        raise Exception("Password does not match all the criterias")

try:
    password_policy_check("Karel", "Karel124$.saAAA")
except Exception as e:
    print(e)
    