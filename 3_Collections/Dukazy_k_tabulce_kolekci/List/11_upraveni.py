"""
There are several methods to update a string element
"""
chameleon = [1, 2, 3, 4, 5]

print(f"This is the list at the begining: {chameleon}")

print()

print("First method is to update an element at a specific index")
chameleon[1] = "Green"
print(f"This is the list now: {chameleon}")

print()

print("You can also update a range of elements")
chameleon[2:3] = ["Black", "White"]
print(f"This is the list now: {chameleon}")