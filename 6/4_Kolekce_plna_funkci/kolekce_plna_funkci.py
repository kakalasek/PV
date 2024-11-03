from random import randint

def space_is_smiley_face(text: str) -> str:
    return text.replace(' ', ':)')

def V_is_W(text: str) -> str:
    return text.replace('V', 'W')

def start_and_end_star(text: str) -> str:
    return "*" + text + "*"

def questionmark_and_explanationmark_change(text: str) -> str:
    return text.replace("?", "???").replace("!", "!!!")

funky_functions = [str.upper, space_is_smiley_face, V_is_W, start_and_end_star, questionmark_and_explanationmark_change]

def funky_format(text: str):
    for i in range(0,3):
        random_pick = randint(0,4)
        text = funky_functions[random_pick](text)
    return text


print(funky_format("Ahoj Karle! Pudeme dnes do kina?"))