"""
There are a few methods to check if a list contains a certain value
"""
lst = [1, 'hey', 3.12]

print("Fist we will use the 'in' keyword ")
if 1 in lst:
    print("1 is in the list")

print()

print("Now we will use the count() method")
if lst.count(3.12) > 0:
    print("3.12 is in the list")