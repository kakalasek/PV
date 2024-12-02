from re import match, search

def count_words(text: str) -> int:
    num_of_words = 0

    while True:
        find = search(r"(January|February|March|April|May|June|July|August|September|October|November|December) [0-9]{1,2}th [0-9]{1,4}[.,;]*", text)
        if find:
            num_of_words += 1
            text = text.replace(find.group(), '', 1)
            continue
        break

    #TODO Implement address checking, they count as one word

    text = text.split(' ')

    #Finding and removing numbers, since they are not a word
    for word in text:
        if word == '':
            continue
        if word.isnumeric():
            continue
        if word.lower() == "can't":
            num_of_words += 1
            continue
        if "'" in word:
            num_of_words += 2
            continue


        num_of_words += 1
    return num_of_words

print(count_words("I'm going to kill myself in September 9th 2005. Can't"))