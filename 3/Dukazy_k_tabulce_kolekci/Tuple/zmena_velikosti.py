"""
Tuple cannot be changed after creation. It throws an error if we try. It does not even have a method to do this
"""
try:
    t = (1, 2, "hell")
    tuple_methods = []
    for method in dir(t):
        if "__" not in method:
            tuple_methods.append(method)

    print(f"Tuple methods: {tuple_methods}")
    t += 1
except:
    print("You cannot add an element into a tuple after creation")

