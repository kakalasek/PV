def tuple_order():
    """
    FALSE

    You cant add new element into an already created tuple 
    """
    t = ("hello", "there")
    print(dir(t))

def list_order():
    """
    TRUE

    If we just add an element to list without specifying the position, it will be appended to the end, thus preserving the order  
    """
    l = ["hello", "there"]
    print(l)
    l.append("general Kenobi")
    print(l)

def set_order():
    """
    FALSE

    The elements are unordered, you cannot be sure in which order they appear

    Run this function few times and you will see
    """
    s = {1, 5, 3, 6, "hell"}
    print(s)
    s.add("toho")
    print(s)

def dictionary_order():
    """
    TRUE

    If we add an element with a key and value, it is simply appeded to the end, thus preserving the order
    """
    d = {"a": 1, "b": 2, "c": 3}
    print(d)
    d["d"] = 4
    print(d)

def string_order():
    """
    TRUE

    If we add a string it just gets appended to the end, if we dont specify otherwise, thus preserving the order 
    """
    s = "Hello there"
    print(s)
    s += " general Kenobi"
    print(s)

##########################################

def tuple_is_ordered():
    pass

def list_is_ordered():
    pass

def set_is_ordered():
    pass

def dictionary_is_ordered():
    pass

def string_is_ordered():
    pass

#########################################

def tuple_is_indexed():
    """
    TRUE

    You can access tuple elements with an index 
    """
    t = ("Hello", "There")
    print(t[0])

def list_is_indexed():
    """
    TRUE

    You can access list elements with an index 
    """
    l = ["Hello", "There"]
    print(l[0])

def set_is_indexed():
    """
    FALSE

    Sets are unordered and unindexed, so no 
    """
    try:
        s = {"Hello", "There"}
        print(s[0])
    except:
        print("Cannot acces set with an index")

def dictionary_is_indexed():
    """
    FALSE

    Dictionary elements need to be accessed with a key, not index 
    """
    try:
        d = {"a": 1, "b": "Hello"}
        print(d[0])
    except:
        print("Cannot access dictionary with an index")

def string_is_indexed():
    """
    TRUE

    String is essentially just a list containing chars or strings, so yes, it can be accessed with an index 
    """
    s = "Hello there"
    print(s[0])

###################################

def tuple_same_elements():
    """
    TRUE

    There is no reason why there couldnt be same elements in a tuple
    """
    t = (1, 1)
    print(t)

def list_same_elements():
    """
    TRUE

    There is no reason why there couldnt be same elements in a list
    """
    l = [1, 1]
    print(l)

def set_same_elements():
    """
    FALSE

    If you try to add already existing element to a set, it wont be added
    """
    s = {1}
    s.add(1)
    print(s)

def dictionary_same_elements():
    """
    TRUE and FALSE

    You can have multiple same values, but keys need to be distinct
    """
    d = {"a": 1, "b": 1}
    print(d)
    d["a"] = 2
    print(d)
    dd = {"a": 1, "a": 2}
    print(dd)

def string_same_elements():
    """
    TRUE

    There is no reason why there couldnt be same elements in a list
    """
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(s)