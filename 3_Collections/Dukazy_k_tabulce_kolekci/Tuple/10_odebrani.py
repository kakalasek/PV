"""
Well, a tuple should be unchangable after creation. So you cannot delete an element without creating a new object.
If you dont care about creating a new object, you can remove an element in a special way with list conversion
"""
not_really_changeble_tuple = (1, 2, 3, 4)

print(f"This is the tuple now: {not_really_changeble_tuple}")
print(f"And this is its id: {id(tuple)}")

print()

print(f"If we convert the tuple into a list, remove an element, it kinda works, but a new object will be created")
not_really_changeble_tuple = list(not_really_changeble_tuple)
not_really_changeble_tuple.pop()
not_really_changeble_tuple = tuple(not_really_changeble_tuple)
print(f"This is the tuple after removing an element: {not_really_changeble_tuple}")
print(f"And this is its new id: {id(not_really_changeble_tuple)}")

print()

print("A tuple does not even have a method to remove an element")
tuple_methods = []
for method in dir(tuple):
    if "__" not in method:
        tuple_methods.append(method)

print(f"Tuple methods: {tuple_methods}")