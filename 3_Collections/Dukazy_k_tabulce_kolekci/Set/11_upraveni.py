"""
Set is unordered and unidexed, thus there is no way to update a specific element
"""

print("A set does not even have a method to update an element")
set_methods = []
for method in dir(set):
    if "__" not in method:
        set_methods.append(method)

print(f"Set methods: {set_methods}")

print()

print("Note that the 'update' method is used to add an element rather than update one")