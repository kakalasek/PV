"""
Tuple cannot be changed after creation. It does not even have a method to do this. We can kinda overcome this with casting it into a list and back, but is wont
be the same object. Same goes for concatenating two tuples
"""
t = (1, 2, "hell")

print("Tuple does not have a method to add an element, thus its size cannot change.")
tuple_methods = []
for method in dir(t):
    if "__" not in method:
        tuple_methods.append(method)

print(f"Tuple methods: {tuple_methods}")

print()


print("We can kinda overcome this by casting it to list, changing its size and casting it back, but it wont be the same object again")
print(f"Tuple before: {t}\n Id before: {id(t)}")
t = list(t)
t.append('')
t = tuple(t)
print(f"Tuple after: {t}\n Id after: {id(t)}")

print()

print("Another method is to concatenate two tuples. Yet once again, the resulting tuple wont be the same object")
print(f"Tuple before: {t}\n Id before: {id(t)}")
t += (1,)
print(f"Tuple after: {t}\n Id after: {id(t)}")

