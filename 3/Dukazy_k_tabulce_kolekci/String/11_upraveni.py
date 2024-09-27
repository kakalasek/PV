"""
Like with removing, you cannot really update an element inside a string, since strings are immutable. You are just creating a new object. Replace() is one of the methods, which can be used
"""
super_string = "I am very super"

print(f"This is the original string: {super_string}")
print(f"This is the original id: {id(super_string)}")
super_string = super_string.replace("e", "X")
print(f"This is the new string: {super_string}")
print(f"This is the new id: {id(super_string)}")
