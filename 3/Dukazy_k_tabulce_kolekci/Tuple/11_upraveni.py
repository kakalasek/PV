"""
By normal means, you cannot update any value in a tuple, without creating a new object. It can once again be kinda cheated through the list conversion, but I am too lazy to include it here also
"""
try:
    you_shall_not_change_me = ("No", "Chance")

    print("I am now going to try to change an element inside a tuple")

    you_shall_not_change_me[1] = 0

except:
    print("This just does not work")

print()

print("A tuple does not even have a method to update an element")
tuple_methods = []
for method in dir(tuple):
    if "__" not in method:
        tuple_methods.append(method)

print(f"Tuple methods: {tuple_methods}")