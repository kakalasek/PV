"""
We can either check for keys or for values. There are several methods for both
"""
ac_dc = {"a": 1, "b": 2, "c": 3}

print("First option is to use the 'in' keyword")
if "a" in ac_dc.keys():
    print("'a' is present in keys of the dict")
if 1 in ac_dc.values():
    print("1 is present in values of the dict")

print()

print("We can check for keys with the get() method")
if ac_dc.get('c'):
    print("'c' is a key in the dict")