"""
Okay, there are quite some methods to see if an element is present in a set. I will list only some of them
"""
sst = {1, (1,2), "One"}

print("You can use the 'in' keyword")
if 1 in sst:
    print("1 is present in the set")

print()

print("You can also check if somehting is a subset of the original set")
if {"One"}.issubset(sst):
    print("'One' is present in the set")

print()

print("There are more methods to do this, I am too lazy to list them all ..")