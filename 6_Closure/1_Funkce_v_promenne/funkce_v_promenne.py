def append_jecna_postfix(username: str) -> str:
    return username + "@spsejecna.cz"

def append_seznam_postfix(username: str) -> str:
    return username + "@seznam.cz"

appender_postfix = append_seznam_postfix

print(appender_postfix('novak'))

