def create_email(appender_function, username):
    return appender_function(username)

def append_jecna_postfix(username: str) -> str:
    return username + "@spsejecna.cz"

def append_seznam_postfix(username: str) -> str:
    return username + "@seznam.cz"

appender_postfix = append_jecna_postfix
print(create_email(appender_postfix, "novak"))
#ma vratit novak@spsejecna.cz
appender_postfix = append_seznam_postfix
print(create_email(appender_postfix, "novak"))
#ma vratit novak@seznam.cz